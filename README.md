# bad-notes

O que o script principal faz?

1. Inicia um servidor local com `http.server` do Python;
2. Converte arquivos modificados em texto de Markdown + LaTeX para HTML + MathJax usando Pandoc;
3. Insere o HTML num template com formatação customizada (style.css) e os scripts necessários;
4. Atualiza a página aberta automaticamente com [Live.js](http://livejs.com/).
