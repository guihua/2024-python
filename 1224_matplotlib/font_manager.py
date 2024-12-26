import matplotlib.font_manager as fm

# 列出所有字体
for font in fm.findSystemFonts(fontpaths=None, fontext='ttf'):
    print(font)