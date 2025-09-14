# Detecção de Pastas e Ícones com OpenCV
Este projeto utiliza **OpenCV em Python** para identificar automaticamente pastas de aplicativos em capturas de tela de celulares e verificar se o **Google Chrome** está presente dentro delas. O fluxo é dividido em duas etapas principais: (1) detecção da pasta, onde filtros como **CLAHE, Canny automático, operações morfológicas e filtros de contorno** são aplicados para gerar uma bounding box verde que isola a pasta mesmo em cenários de baixo contraste; e (2) identificação do ícone do Chrome, onde é aplicado **Template Matching** comparando os ícones internos com uma imagem de referência do Chrome. Se o Chrome for encontrado, a imagem processada é salva na pasta `com_chrome`, caso contrário, vai para `sem_chrome`.  

O projeto foi estruturado para ser simples e fácil de expandir. A detecção de pastas garante robustez em diferentes fundos (claros ou escuros) e a identificação de ícones serve como exemplo prático de como aplicar técnicas clássicas de visão computacional a problemas reais do dia a dia.  

## Requisitos
- Python 3.8+  
- OpenCV  
- NumPy  

Instalação das dependências:  
```bash
pip install opencv-python numpy
```

## Estrutura de Pastas
```
.
├── icon/                # Template dos ícones (ex.: chrome_template.png)
├── dataset/                # Screenshots de entrada
├── resultado/
│   ├── com_chrome/       # Resultados quando o Chrome é encontrado
│   └── sem_chrome/       # Resultados quando não há Chrome
    └── bound_box/        # Resultados com a pasta identificada       
├── detectar.py           # Funções que são usadas no programa
├── main.py               # Programa principal
└── README.md
```

## Exemplo
**Input:** captura de tela contendo uma pasta de aplicativos.  
**Output:** bounding box verde ao redor da pasta e, quando o Chrome é encontrado, retângulo vermelho em volta do ícone.  

## Melhorias Futuras
- Detectar múltiplos ícones além do Chrome (YouTube, Drive, etc.).  
- Utilizar **Feature Matching (ORB/SIFT)** para maior robustez em diferentes tamanhos/cores.  
- Treinar um modelo leve de classificação de ícones usando CNN.  

## Autor
Projeto desenvolvido por Misael Ricardo para estudo de visão computacional e automação com OpenCV, mostrando como técnicas clássicas podem ser aplicadas em cenários reais de forma prática e eficiente.  
