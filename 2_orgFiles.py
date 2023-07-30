# import required module
import os
# assign directory
dir_parent = '01156917'

sub_dirs = [
    'RUN1_HK_START_TOP',
    'RUN1_HK_END_TOP',
    'RUN2_HK_START_TOP',
    'RUN2_HK_END_TOP',
    'RUN3_HK_START_TOP',
    'RUN3_HK_END_TOP',
    'RUN4_HK_START_TOP',
    'RUN4_HK_END_TOP',
    'RUN5_HK_START_TOP',
    'RUN5_HK_END_TOP',        
    'RUN6_HK_START_TOP',
    'RUN6_HK_END_TOP',
    'RUN7_HK_START_TOP',
    'RUN7_HK_END_TOP',
    'RUN8_HK_START_TOP',
    'RUN8_HK_END_TOP',
]

for sd in sub_dirs:
    directory = dir_parent+'/'+sd+'/'
    newFilename = sd+'.js'

    hosts = [
        ['iapp661','shard1_661'],
        ['iapp1478','shard2_1478'],
        ['iapp1479','shard3_1479'],
        ['iapp1480','shard4_1480'],
        ['iapp1481','shard5_1481'],
        ['iapp1482','shard6_1482'],
        ['iapp1100','shard7_1100'],
        ['iapp1101','shard8_1101'],
        ['iapp1103','shard9_1103'],
        ['iapp660','shard10_660'],   
        ['iapp694','shard11_694'],
        ['iapp662','shard12_662'],
        ['iapp663','shard13_663'],
        ['iapp664','shard14_664'],
        ['iapp665','shard15_665'],
        ['iapp666','shard16_666'],
        ['iapp667','shard17_667'],
        ['iapp668','shard18_668'],
        ['iapp696','shard19_696'],
        ['iapp697','shard20_697'], 
        ['iapp1483','shard21_1483'],
        ['iapp1484','shard22_1484'],
        ['iapp1485','shard23_1485'],
        ['iapp1535','shard24_1535'],
        ['iapp1536','shard25_1536'],
        ['iapp1537','shard26_1537'],
        ['iapp3540','shard27_3540'],
        ['iapp3541','shard28_3541'],
        ['iapp3535','shard29_3535'],
        ['iapp3536','shard30_3536'], 
        ['iapp3537','shard31_3537'],
        ['iapp3538','shard32_3538'],
        ['iapp3560','shard33_3560'],
        ['iapp3561','shard34_3561'],
        ['iapp3562','shard35_3562'],
        ['iapp3857','shard36_3857'],
        ['iapp3858','shard37_3858'],
        ['iapp3859','shard38_3859'],
        ['iapp3860','shard39_3860'],
        ['iapp3861','shard40_3861'], 
        ['iapp3862','shard41_3862'],
        ['iapp3863','shard42_3863'],
        ['iapp3864','shard43_3864'],
        ['iapp3865','shard44_3865'],
        ['iapp3866','shard45_3866'],
        ['iapp3867','shard46_3867'],
        ['iapp3868','shard47_3868'],
        ['iapp4290','shard48_4290'],
        ['iapp4291','shard49_4291'],
        ['iapp4260','shard50_4260'], 
        ['iapp4261','shard51_4261'],
        ['iapp4262','shard52_4262'],
        ['iapp4263','shard53_4263'],
        ['iapp4268','shard54_4268'],
        ['iapp4269','shard55_4269'],
        ['iapp4270','shard56_4270'],
        ['iapp4288','shard57_4288'],
        ['iapp4271','shard58_4271'],
        ['iapp4272','shard59_4272'],
        ['iapp4273','shard60_4273'], 
        ['iapp4274','shard61_4274'],
        ['iapp5041','shard62_5041'],
        ['iapp5042','shard63_5042'],
        ['iapp5043','shard64_5043'],
        ['iapp5038','shard65_5038'],
        ['iapp4321','shard66_4321'],
        ['iapp4322','shard67_4322'] 
    ]

    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            for host in hosts:
                if host[0] in filename: 
                    #shutil.move(filename, "../"+host[1]+"/"+filename)
                    #os.rename(filename, "shard_output/"+host[1]+"/"+newFilename)
                    os.rename(directory+filename, "shard_output/"+host[1]+"/"+newFilename)
