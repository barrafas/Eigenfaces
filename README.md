# Eigenfaces - EN

A linear algebra and numpy project to learn more about how eigenfaces work and try out some of their many applications.

We defined some functions in the code to easily let anyone test the algorithm with their own images. Do note that the images being inserted into the program need to have a bit-depth of 8, otherwise they'll be read as an entirely black image. To circunvent that, try converting it into a .jpg on the following site: https://convert-my-image.com/ImageConverter_Pt

## Contents:
* `alternate_data`: Alternate dataset we used for testing after failed attempts with the original one.
It belongs to AT&T Laboratories Cambridge.

* `alternate_testing`: Testing images related to the alternate dataset

* `data`: Main dataset we used for testing.
It is an edited version of the "Labeled Faces in the Wild" dataset, found in https://conradsanderson.id.au/lfwcrop/. Moreover, we also filtered it out to only have images of people who had at least 8 images originally.

* `testing`: Testing images related to the main dataset.

* `eigenfaces_alternate.ipynb`: Testing we did on the alternate dataset.

* `eigenfaces_alternate.ipynb`: The main code file for our entire analysis.

* `eigenfaces_relatorio.pdf`: The project's report, only available in Portuguese.

* `eigenfaces_slides.pdf`: The project's slideshow presentation, only available in Portuguese.


# Eigenfaces - PT

Um projeto de álgebra linear e numpy feito para aprender mais sobre como as eigenfaces funcionam e testar algumas de suas aplicações.

Nós definimos algumas funções no código para permitir que qualquer pessoa possa testar o algoritmo facilmente com suas próprias imagens. É importante notar que as imagens sendo inseridas no programa têm que ter uma intensidade de bits de 8, se não elas serão lidas como um quadrado preto. Para evitar isso, converta a imagem em um .jpg no site a seguir: https://convert-my-image.com/ImageConverter_Pt

## Conteúdo:
* `alternate_data`: Dataset alternativo usado após o dataset original não ter nos dado resultados satisfatórios na testagem.
Pertence ao AT&T Laboratories Cambridge.

* `alternate_testing`: Imagens de teste associadas ao dataset alternativo.
 
* `data`: Dataset principal usado para os testes.
É uma versão editada do dataset "Labeled Faces in the Wild", encontrada no link https://conradsanderson.id.au/lfwcrop/. Também a filtramos para ter somente imagens de pessoas que possuiam 8 ou mais imagens originalmente.

* `testing`: Imagens de teste associadas ao dataset principal.

* `eigenfaces_alternate.ipynb`: Arquivo de testes no dataset alternativo.

* `eigenfaces_alternate.ipynb`: Arquivo principal de código de nossa análise e algoritmo com base no dataset original.

* `eigenfaces_relatorio.pdf`: Relatório do projeto.

* `eigenfaces_slides.pdf`: Apresentação em slides do projeto.
