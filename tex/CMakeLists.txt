include(UseLATEX)

add_latex_document(introduction.tex TARGET_NAME introduction)
add_latex_document(theory.tex
                   INPUTS integral-geometry.tex liquid-state-theory.tex supercooled-liquids.tex
                   TARGET_NAME theory)
add_latex_document(morphometric-framework.tex TARGET_NAME morph1)
add_latex_document(morphometric-applications.tex TARGET_NAME morph2)
add_latex_document(cuzr.tex TARGET_NAME cuzr)
add_latex_document(aerosols.tex TARGET_NAME aerosols)
add_latex_document(conclusion.tex TARGET_NAME conclusion)

add_custom_target(chapters)
add_dependencies(chapters introduction theory morph1 morph2 cuzr aerosols conclusion)

add_latex_document(thesis.tex
                   INPUTS abstract.tex dedication.tex declaration.tex acknowledgements.tex introduction.tex theory.tex integral-geometry.tex liquid-state-theory.tex supercooled-liquids.tex morphometric-framework.tex morphometric-applications.tex cuzr.tex aerosols.tex conclusion.tex
                   TARGET_NAME thesis)

add_custom_command(TARGET chapters POST_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy
                   ${CMAKE_CURRENT_BINARY_DIR}/*.pdf
                   ${CMAKE_BINARY_DIR}/)

add_custom_command(TARGET thesis POST_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy
                   ${CMAKE_CURRENT_BINARY_DIR}/*.pdf
                   ${CMAKE_BINARY_DIR}/)
