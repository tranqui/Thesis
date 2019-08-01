include(UseLATEX)

add_latex_document(introduction.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME introduction IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(background.tex
                   INPUTS integral-geometry.tex liquid-state-theory.tex density-functional-theory.tex supercooled-liquids.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME background IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(morphometric-framework.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME morph1 IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(morphometric-applications.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME morph2 IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(resummation.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME resummation IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(aerosols.tex
                   BIBFILES bibliography.bib unpublished.bib USE_BIBLATEX
                   TARGET_NAME aerosols IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(conclusion.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME conclusion IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(appendix-spt-singularities.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME appendix-spt-singularities IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(appendix-two-spheres.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME appendix-two-spheres IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(appendix-full-geometry.tex
                   BIBFILES bibliography.bib USE_BIBLATEX
                   TARGET_NAME appendix-full-geometry IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
# add_latex_document(appendix-diagrams.tex
#                    TARGET_NAME appendix-diagrams IMAGE_DIRS ../img EXCLUDE_FROM_ALL)

add_custom_target(chapters)
add_dependencies(chapters introduction background morph1 morph2 resummation aerosols conclusion appendix-spt-singularities appendix-two-spheres appendix-full-geometry)

add_latex_document(thesis.tex
                   INPUTS abstract.tex dedication.tex declaration.tex acknowledgements.tex word-count.tex opening-quote.tex introduction.tex background.tex integral-geometry.tex liquid-state-theory.tex density-functional-theory.tex supercooled-liquids.tex morphometric-framework.tex morphometric-applications.tex resummation.tex aerosols.tex conclusion.tex appendix-spt-singularities.tex appendix-two-spheres.tex appendix-full-geometry.tex
                   BIBFILES bibliography.bib unpublished.bib
                   USE_BIBLATEX
                   TARGET_NAME thesis
                   IMAGE_DIRS ../img)

add_custom_command(TARGET chapters POST_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy
                   ${CMAKE_CURRENT_BINARY_DIR}/*.pdf
                   ${CMAKE_BINARY_DIR}/)

add_custom_command(TARGET thesis POST_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy
                   ${CMAKE_CURRENT_BINARY_DIR}/*.pdf
                   ${CMAKE_BINARY_DIR}/)
