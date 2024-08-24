translation_dictionary = {

    'seams'     : "Corrigir transisões no corpo",
    'seams_tt'  : 'Esta operação realiza a \"remoção de duplos\" nas texturas do corpo. A remoção de duplos também estraga os pesos em determinadas áreas. A desativação desta operação preserva os pesos, mas pode provocar o aparecimento de costuras à volta do pescoço e ao longo do peito',
    
    'outline'     : 'Usar apenas uma silhueta',
    'outline_tt'  : "Permite utilizar apenas um material de silhueta genérico, em vez de utilizar vários materiais únicos. Se selecionar esta opção pode causar problemas de transparência do contorno",
    
    'keep_templates'        : "Manter os modelos de texturas",
    'keep_templates_tt'     : "Mantenha ativado para preservar modelos de texturas, isso previne que sejam deletadas quando o Blender for fechado, é útil caso também queira aplicar as outros objetos",

    'sfw_mode'          : 'modo SWF',
    'sfw_mode_tt'       : 'Tenta esconder algumas partes NSFW do modelo',

    'arm_drop'          : "Tipo de Armature",
    'arm_drop_A'        : "Usar a Armature do KKBP",
    'arm_drop_A_tt'     : "Usar a armature do KKBP. Isso modificará ligeiramente a armature e fornecerá IKs básicos",
    'arm_drop_B'        : "Usar Armature do Rigify",
    'arm_drop_B_tt'     : "Usar a armature do Rigify. Esta é uma armadura avançada adequada para uso no Blender",
    'arm_drop_C'        : "Usar Armature do Koikatsu",
    'arm_drop_C_tt'     : "Usar a armature do Koikatsu padrão. Isso corresponderá à nomenclatura e estrutura de ossos do jogo",
    'arm_drop_D'        : "Usar Armature do PMX",
    'arm_drop_D_tt'     : "Usar a armature padrão do PMX. Esta é a armature que você obtém do exportador KKBP",

    'cat_drop'      : 'Tipo de execução',
    'cat_drop_A'    : "Categorizar automaticamente",
    'cat_drop_A_tt' : "Importar tudo e obter um único objeto contendo todas as roupas de seu modelo. Oculta qualquer roupa alternativa por padrão",
    'cat_drop_B'    : "Pausa para categorizar",
    'cat_drop_B_tt' : "Importe tudo, mas pause para separar manualmente as roupas em grupos de objetos. O cabelo deve ser separado e nomeado como \"Hair\" ou \"hair\". Quando terminar de separar, clique no botão Concluir categorização para finalizar a importação. Oculta qualquer roupa alternativa por padrão",
    'cat_drop_C'    : "Separar todos os objetos",
    'cat_drop_C_tt' : "Importe tudo e separe automaticamente cada peça de roupa em vários objetos",
    'cat_drop_D'    : "Categorizar por dados SMR",
    'cat_drop_D_tt' : "Importe tudo e separe automaticamente cada objeto pelo seu Skinned Mesh Renderer. Nota: Esta opção é apenas para exportar malhas, então não aplicará nenhum modelo de material ou cores",

    'dark'      : "Cores escuras",
    'dark_A'    : "LUT Night",
    'dark_A_tt' : "Torna cores escuras azuladas",
    'dark_B'    : "LUT Sunset",
    'dark_B_tt' : "Torna cores escuras avermelhadas",
    'dark_C'    : "LUT Day",
    'dark_C_tt' : "Faz as cores escuras serem as mesmas das claras",
    'dark_D'    : "Baseado em saturação",
    'dark_D_tt' : "Torna as cores escuras mais saturadas que as claras",
    'dark_E'    : 'Redução de valor',
    'dark_E_tt' : "Tornas as cores escuras mais escuras que as claras",
    'dark_F'    : 'Automático',
    'dark_F_tt' : "Usa um método automático para definir as cores escuras",

    'prep_drop'         : "Tipo de exportação",
    'prep_drop_A'       : "Unity - compatível com VRM",
    'prep_drop_A_tt'    : """Remove o contorno e...
    remove o slot de material do olho branco duplicado se presente,
    edita a hierarquia de ossos para permitir que o Unity detecte automaticamente os ossos corretos""",
    'prep_drop_B'       : "FBX Genérico - Sem mudanças",
    'prep_drop_B_tt'    : """Remove o contorno e...
    remove o slot de material do olho branco duplicado se presente""",
    'prep_drop_D'       : "Unity - compatível com VRChat",
    'prep_drop_D_tt'    : """Remove o contorno e...
    remove o slot de material do olho branco duplicado se presente,
    remove o osso "Upper Chest",
    edita a hierarquia de ossos para permitir que o Unity detecte automaticamente os ossos corretos""",

    'simp_drop'     : 'Armature simplification type',
    'simp_drop_A'   : 'Very simple (SLOW)',
    'simp_drop_A_tt': 'Use this option if you want a very low bone count. Moves the pupil bones to layer 1 and simplifies bones on armature layers 3-5, 11-12, and 17-19 (Leaves you with ~110 bones not counting the skirt bones)',
    'simp_drop_B'   : 'Simple',
    'simp_drop_B_tt': 'Moves the pupil bones to layer 1 and simplifies the useless bones on armature layer 11 (Leaves you with ~1000 bones)',
    'simp_drop_C'   : 'No changes (FAST)',
    'simp_drop_C_tt': 'Does not simplify anything',

    'bake'          : 'Bake material templates',
    'bake_light'    : "Light",
    'bake_light_tt' : "Bake light version of all textures",
    'bake_dark'     : "Dark",
    'bake_dark_tt'  : "Bake dark version of all textures",
    'bake_norm'     : "Normal",
    'bake_norm_tt'  : "Bake normal version of all textures",
    'bake_mult'     : 'Bake multiplier',
    'bake_mult_tt'  : "Set this to 2 or 3 if the baked texture is blurry",
    'old_bake'      : 'Use old baker',
    'old_bake_tt'   : 'Enable to use the old baking system. This system will not bake any extra UV maps like hair shine or eyeshadow',

    'shape_A'       : 'Use KKBP shapekeys',
    'shape_A_tt'    : 'Rename and delete the old shapekeys. This will merge the shapekeys that are part of the same expression and delete the rest',
    'shape_B'       : "Save partial shapekeys",
    'shape_B_tt'    : "Save the partial shapekeys that are used to generate the KK shapekeys. These are useless on their own",
    'shape_C'       : "Skip modifying shapekeys",
    'shape_C_tt'    : "Use the stock Koikatsu shapekeys. This will not change the shapekeys in any way",

    'shader_A'       : 'Use Eevee',
    'shader_B'       : "Use Cycles",
    'shader_C'       : "Use Eevee mod",
    'shader_C_tt'    : "Uses a modified shader setup for Eevee",

    'atlas'         : 'Atlas type',

    'export_fbx'    : 'Export FBX',
    'export_fbx_tt' : 'Exports all visible objects as an fbx file. This is the same as the FBX export function in the File menu',

    'import_export' : 'Importing and Exporting',
    'import_model'  : 'Import model',
    'finish_cat'    : 'Finish categorization',
    'recalc_dark'   : 'Recalculate dark colors',
    'prep'          : 'Prep for target application',
    'apply_temp'    : 'Switch baked templates',

    'studio_object'             : 'Import studio object',
    'animation_library'         : 'Create animation library',
    'animation_library_tt'      : "Creates an animation library using the current file and current character. Will not save over the current file in case you want to reuse it. Open the folder containing the animation files exported with SB3Utility",
    'animation_library_scale'   : 'Scale arms',
    'animation_library_scale_tt': 'Check this to scale the arms on the y axis by 5%. This will make certain poses more accurate to the in-game one',
    'map_library'               : 'Create map asset library',
    'map_library_tt'            : "Creates an asset library using ripped map data. Open the folder containing the map files exported with SB3Utility. Takes 40 to 500 seconds per map",
    'finalize_materials'        : 'Optimize materials',
    'finalize_materials_tt'     : """!! Bake your materials, then use the 'Switch baked' button for 'Light' and 'Dark' before using this button !!
    Replaces the KKBP node groups with a simple mix node to increase animation playback performance. Backups are saved as '-ORG'""",

    'rigify_convert': "Convert for Rigify",
    'sep_eye'       : "Separate Eyes and Eyebrows",

    'convert_image' : 'Convert image with KKBP',

    'kkbp_import_tt'   : "Imports a Koikatsu model (.pmx format) and applies fixes to it",
    'mat_import_tt'     : "Finish separating objects, apply the textures and colors",
    'export_prep_tt'    : "Check the dropdown for more info",
    'bake_mats_tt'      : "Open the folder you want to bake the material templates to",
    'apply_mats_tt'     : "Open the folder that contains the baked materials. Use the menu to load the Light / Dark / Normal passes",
    'import_colors_tt'  : "Open the folder containing your model.pmx file to recalculate the dark colors",
}
