MAIN='main'

pdflatex --shell-escape ${MAIN}  
biber    --shell-escape ${MAIN}  
pdflatex --shell-escape ${MAIN}  
pdflatex --shell-escape ${MAIN} 

exit 0 
