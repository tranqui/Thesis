include(UseLATEX)

add_latex_document(introduction.tex TARGET_NAME introduction IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(integral-geometry.tex TARGET_NAME geometry IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(theory.tex
                   INPUTS liquid-state-theory.tex supercooled-liquids.tex
                   TARGET_NAME theory IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(morphometric-framework.tex TARGET_NAME morph1 IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(morphometric-applications.tex TARGET_NAME morph2 IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(cuzr.tex TARGET_NAME cuzr IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(aerosols.tex TARGET_NAME aerosols IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(conclusion.tex TARGET_NAME conclusion IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(appendix-two-spheres.tex TARGET_NAME appendix-two-spheres IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(appendix-full-geometry.tex
                   INPUTS appendix-line-curvature.tex
                   TARGET_NAME appendix-full-geometry IMAGE_DIRS ../img EXCLUDE_FROM_ALL)
add_latex_document(appendix-finite-differences.tex TARGET_NAME appendix-finite-differences IMAGE_DIRS ../img EXCLUDE_FROM_ALL)

add_custom_target(chapters)
add_dependencies(chapters introduction geometry theory morph1 morph2 cuzr aerosols conclusion appendix-two-spheres appendix-full-geometry appendix-finite-differences)

add_latex_document(thesis.tex
                   INPUTS abstract.tex dedication.tex declaration.tex acknowledgements.tex word-count.tex introduction.tex integral-geometry.tex theory.tex liquid-state-theory.tex supercooled-liquids.tex morphometric-framework.tex morphometric-applications.tex cuzr.tex aerosols.tex conclusion.tex appendix-two-spheres.tex appendix-full-geometry.tex appendix-line-curvature.tex appendix-finite-differences.tex
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
