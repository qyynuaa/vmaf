feature_dict = {

    'VMAF_feature': ['vif_scale0', 'vif_scale1', 'vif_scale2', 'vif_scale3',
                     'adm_scale0', 'adm_scale1', 'adm_scale2', 'adm_scale3',
                     'motion'],

}

model_type = "LIBSVMNUSVR"
model_param_dict = {

    # ==== preprocess: normalize each feature ==== #

    'norm_type': 'clip_0to1', # rescale to within [0, 1]

    # 'norm_type': 'custom_clip_0to1', # linearly map the range specified to [0, 1]; if unspecified, use clip_0to1
    # 'custom_clip_0to1_map': {
    #     'VMAF_feature_adm_scale0_score': [0.0, 0.5],
    # },

    # ==== postprocess: clip final quality score ==== #
    # 'score_clip': None, # default: do nothing
    'score_clip': [0.0, 100.0], # clip to within [0, 100]

    # ==== libsvmnusvr parameters ==== #

    # 'gamma': 0.0, # default
    'gamma': 0.05, #vmaf_v3, vmaf_v4, vmaf_v5

    # 'C': 1.0, # default
    'C': 4.0, # vmaf_v4, vmaf_v5

    # 'nu': 0.5, # default
    'nu': 0.9, # vmafv4, vmaf_v5
}
