import os
directory = "shard_output"

path = os.path.join("./", directory)
os.mkdir(path)

shards = [
    'shard1_661','shard2_1478','shard3_1479','shard4_1480','shard5_1481','shard6_1482','shard7_5166','shard8_5167','shard9_5168','shard10_660',
    'shard11_694','shard12_662','shard13_663','shard14_664','shard15_665','shard16_666','shard17_667','shard18_668','shard19_696','shard20_697',
    'shard21_1483','shard22_1484','shard23_1485','shard24_1535','shard25_1536','shard26_1537','shard27_3540','shard28_3541','shard29_3535','shard30_3536',
    'shard31_3537','shard32_3538','shard33_3560','shard34_3561','shard35_3562','shard36_3857','shard37_3858','shard38_3859','shard39_3860','shard40_3861',
    'shard41_3862','shard42_3863','shard43_3864','shard44_3865','shard45_3866','shard46_3867','shard47_3868','shard48_4290','shard49_4291','shard50_4260',
    'shard51_4261','shard52_4262','shard53_4263','shard54_4268','shard55_4269','shard56_4270','shard57_4288','shard58_4271','shard59_4272','shard60_4273',
    'shard61_4274','shard62_5041','shard63_5042','shard64_5043','shard65_5038','shard66_4321','shard67_4322','shard68_4583','shard69_4584','shard70_4602',
    'shard71_4603','shard72_4604','shard73_4605','shard74_4606','shard75_4607','shard76_4608','shard77_4609'
]

for sh in shards:
    path = os.path.join("./"+directory+"/", sh)
    os.mkdir(path)
