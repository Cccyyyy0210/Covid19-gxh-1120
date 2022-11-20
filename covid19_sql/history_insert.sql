create table history
(
    ds           datetime   not null comment '日期'
        primary key,
    confirm      int        null comment '累计确诊',
    heal         int        null comment '累计治愈',
    dead         int        null comment '累计死亡',
    nowConfirm   int        null comment '现有确诊',
    noInfectH5   int        null comment '现有无症状',
    nowSevere    int        null comment '现有重症',
    localConfirm int        null comment '现有本土',
    importedCase int        null comment '累计境外输入',
    deadRate     varchar(5) null comment '死亡率',
    healRate     varchar(5) null comment '治愈率'
);

INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-11 00:00:00', 6296680, 328514, 25275, 5942891, 22555, 24, 5403, 23012, '0.4', '5.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-12 00:00:00', 6330038, 329059, 25237, 5975742, 21919, 25, 5083, 23074, '0.4', '5.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-13 00:00:00', 6356783, 330119, 25354, 6001310, 21298, 0, 4851, 23128, '0.4', '5.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-14 00:00:00', 6404975, 330683, 25381, 6048911, 20832, 0, 4714, 23169, '0.4', '5.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-15 00:00:00', 6455788, 331569, 25428, 6098791, 20206, 0, 4334, 23210, '0.4', '5.1');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-16 00:00:00', 6502479, 332770, 25491, 6144218, 19229, 0, 3681, 23269, '0.4', '5.1');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-17 00:00:00', 6545234, 333459, 25553, 6186222, 18148, 0, 3502, 23333, '0.4', '5.1');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-18 00:00:00', 6585920, 334196, 25609, 6226115, 17756, 0, 3293, 23381, '0.4', '5.1');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-19 00:00:00', 6626392, 334905, 25671, 6265816, 17213, 0, 3070, 23436, '0.4', '5.1');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-20 00:00:00', 6655661, 335458, 25712, 6294491, 16241, 0, 2881, 23484, '0.4', '5.0');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-21 00:00:00', 6701113, 336141, 25744, 6339228, 14762, 0, 2726, 23527, '0.4', '5.0');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-22 00:00:00', 6748819, 336817, 25792, 6386210, 14010, 0, 2606, 23578, '0.4', '5.0');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-23 00:00:00', 6792066, 337499, 25868, 6428699, 13518, 0, 2494, 23632, '0.4', '5.0');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-24 00:00:00', 6833790, 338018, 26074, 6469698, 11627, 0, 2477, 23691, '0.4', '4.9');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-25 00:00:00', 6872895, 339014, 26132, 6507749, 11515, 0, 2395, 23749, '0.4', '4.9');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-26 00:00:00', 6912675, 339556, 26176, 6546943, 10573, 0, 2404, 23809, '0.4', '4.9');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-27 00:00:00', 6942179, 339982, 26244, 6575953, 10414, 0, 2381, 23881, '0.4', '4.9');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-28 00:00:00', 6988610, 340385, 26278, 6621947, 10373, 0, 2378, 23956, '0.4', '4.9');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-29 00:00:00', 7037863, 340869, 26330, 6670664, 10105, 0, 2365, 24020, '0.4', '4.8');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-09-30 00:00:00', 7083359, 341316, 26388, 6715655, 9829, 0, 2359, 24079, '0.4', '4.8');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-01 00:00:00', 7127469, 341798, 26446, 6759225, 9770, 0, 2301, 24145, '0.4', '4.8');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-02 00:00:00', 7171159, 342283, 26500, 6802376, 9618, 0, 2905, 24208, '0.4', '4.8');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-03 00:00:00', 7215114, 123515, 26568, 7065031, 8814, 0, 2306, 24259, '0.4', '1.7');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-04 00:00:00', 7249310, 343137, 26609, 6879564, 8449, 0, 2341, 24316, '0.4', '4.7');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-05 00:00:00', 7299603, 343707, 26648, 6929248, 8109, 0, 2261, 24366, '0.4', '4.7');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-06 00:00:00', 7355347, 344104, 26706, 6984537, 8069, 0, 2263, 24412, '0.4', '4.7');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-07 00:00:00', 7402656, 344521, 26769, 7031366, 8744, 0, 2329, 24484, '0.4', '4.7');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-08 00:00:00', 7454504, 344931, 26823, 7082750, 9419, 0, 2666, 24538, '0.4', '4.6');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-09 00:00:00', 7499946, 345374, 26912, 7127660, 10193, 0, 2977, 24600, '0.4', '4.6');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-10 00:00:00', 7545527, 345754, 26977, 7172796, 11206, 0, 3240, 24661, '0.4', '4.6');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-11 00:00:00', 7578751, 346151, 27044, 7205556, 11944, 0, 3460, 24725, '0.4', '4.6');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-12 00:00:00', 7621171, 346611, 27089, 7247471, 474, 0, 3637, 24768, '0.4', '4.5');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-13 00:00:00', 7674690, 347107, 27135, 7300448, 13455, 0, 3779, 24818, '0.4', '4.5');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-14 00:00:00', 7729043, 347590, 27172, 7354281, 13998, 0, 3824, 24882, '0.4', '4.5');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-15 00:00:00', 7778306, 348087, 27259, 7402960, 14442, 0, 3906, 24952, '0.4', '4.5');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-16 00:00:00', 7822739, 348624, 27343, 7446772, 14606, 0, 3854, 25022, '0.3', '4.5');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-17 00:00:00', 7865269, 349111, 27413, 7488745, 442, 0, 3808, 25085, '0.3', '4.4');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-18 00:00:00', 7895059, 349577, 27471, 7518011, 14750, 0, 3777, 25127, '0.3', '4.4');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-19 00:00:00', 7940813, 350092, 27511, 7563210, 14715, 0, 3677, 25170, '0.3', '4.4');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-20 00:00:00', 7986272, 350664, 27565, 7608043, 14774, 0, 3595, 25217, '0.3', '4.4');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-21 00:00:00', 8026778, 351194, 27666, 7647918, 14658, 0, 3529, 25273, '0.3', '4.4');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-22 00:00:00', 8064765, 351795, 27753, 7685217, 14360, 0, 3362, 25329, '0.3', '4.4');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-23 00:00:00', 8101522, 352340, 27812, 7721370, 14193, 0, 3245, 25381, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-24 00:00:00', 8137786, 352868, 27881, 7757037, 845, 0, 3179, 25429, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-25 00:00:00', 8165043, 353392, 27950, 7783701, 14026, 0, 3062, 25470, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-26 00:00:00', 8205171, 353910, 28002, 7823259, 14399, 0, 3127, 25511, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-27 00:00:00', 8246496, 354455, 28061, 7863980, 14475, 0, 3104, 25549, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-28 00:00:00', 8283181, 354947, 28153, 7900081, 14817, 0, 3107, 25597, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-29 00:00:00', 8318921, 355417, 28217, 7935287, 15140, 0, 3252, 25650, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-30 00:00:00', 8352484, 355864, 28301, 7968319, 15931, 0, 3440, 25698, '0.3', '4.3');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-10-31 00:00:00', 8385213, 356301, 28389, 8000523, 17538, 0, 4216, 25740, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-01 00:00:00', 8409023, 356637, 28460, 8023926, 19036, 0, 4101, 25789, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-02 00:00:00', 8444367, 357103, 28518, 8058746, 20631, 0, 4791, 25845, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-03 00:00:00', 8478830, 357626, 28579, 8092625, 22423, 0, 4641, 25895, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-04 00:00:00', 8510115, 358088, 28670, 8123357, 24734, 0, 5070, 25948, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-05 00:00:00', 8538758, 358644, 28755, 8151359, 26924, 0, 5473, 26009, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-06 00:00:00', 8565587, 359149, 28840, 8177598, 30018, 0, 5792, 26071, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-07 00:00:00', 8591083, 359672, 28900, 8202511, 34158, 0, 6113, 26105, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-08 00:00:00', 8609153, 360050, 28939, 8220164, 39861, 0, 6742, 26152, '0.3', '4.2');
INSERT INTO covid19.history (ds, confirm, heal, dead, nowConfirm, noInfectH5, nowSevere, localConfirm, importedCase, deadRate, healRate) VALUES ('2022-11-09 00:00:00', 8635852, 360541, 28958, 8246353, 45493, 0, 7801, 26204, '0.3', '4.2');
