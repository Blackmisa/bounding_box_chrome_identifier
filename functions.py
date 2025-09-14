import cv2
import numpy as np

def canned(path):

    img = cv2.imread(path)
    H, W = img.shape[:2]

    pad = 30
    img_pad = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)

    gray = cv2.cvtColor(img_pad, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(gray, 75, 225, apertureSize=3, L2gradient=True)

    K = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    edges = cv2.dilate(edges, K, iterations=1)
    edges = cv2.erode(edges,  K, iterations=1)

    cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    area_img = (H+2*pad) * (W+2*pad)
    min_frac, max_frac = 0.015, 0.50
    min_ar, max_ar   = 0.70, 1.40

    best = None
    best_area = 0

    for c in cnts:
        a = cv2.contourArea(c)

        if a < min_frac*area_img or a > max_frac*area_img:
            continue

        x,y,w,h = cv2.boundingRect(c)
        ar = w/float(h)

        if not (min_ar <= ar <= max_ar):
            continue

        if a > best_area:
            best_area = a
            best = (x,y,w,h)

    if best is None:
        return img

    x,y,w,h = best
    x -= pad; y -= pad
    x1 = max(0, x); y1 = max(0, y)
    x2 = min(W-1, x+w); y2 = min(H-1, y+h)

    extra = 2
    x1 = max(0, x1-extra); y1 = max(0, y1-extra)
    x2 = min(W-1, x2+extra); y2 = min(H-1, y2+extra)

    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    return img

def chrome(path, template_path, threshold=0.8):

    img = cv2.imread(path)
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)

    return img, loc
