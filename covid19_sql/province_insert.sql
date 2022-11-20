create table province
(
    id           int auto_increment
        primary key,
    provinceName varchar(20) not null,
    nowConfirm   int         not null,
    confirm      int         null,
    suspect      int         not null,
    heal         int         not null,
    dead         int         not null,
    highRisk     int         not null,
    midRisk      int         not null
);

INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (1, '台湾', 7949084, 7976205, 485, 13742, 13379, 0, 0);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (2, '香港', 337251, 441172, 181, 93420, 10501, 0, 0);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (3, '广东', 3169, 14779, 25, 11602, 8, 161, 174);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (4, '内蒙古', 1088, 5586, 35, 4497, 1, 252, 218);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (5, '山西', 755, 1675, 64, 920, 0, 171, 158);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (6, '河南', 735, 4148, 1, 3391, 22, 96, 231);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (7, '重庆', 605, 1920, 15, 1309, 6, 32, 221);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (8, '福建', 454, 5354, 15, 4899, 1, 87, 235);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (9, '北京', 452, 5107, 164, 4646, 9, 95, 93);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (10, '新疆', 366, 2061, 0, 1692, 3, 1229, 303);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (11, '四川', 277, 6514, 22, 6234, 3, 24, 35);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (12, '湖南', 261, 1816, 2, 1551, 4, 242, 179);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (13, '云南', 171, 2764, 23, 2591, 2, 47, 54);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (14, '陕西', 154, 4218, 4, 4061, 3, 21, 73);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (15, '江苏', 110, 2775, 3, 2665, 0, 0, 7);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (16, '黑龙江', 80, 3571, 430, 3478, 13, 587, 397);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (17, '山东', 76, 3247, 14, 3164, 7, 92, 134);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (18, '天津', 73, 2506, 50, 2430, 3, 31, 45);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (19, '浙江', 55, 3590, 68, 3534, 1, 0, 0);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (20, '甘肃', 42, 1408, 0, 1364, 2, 44, 61);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (21, '上海', 39, 64326, 393, 63692, 595, 0, 9);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (22, '辽宁', 35, 2055, 0, 2018, 2, 78, 111);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (23, '海南', 25, 8983, 18, 8952, 6, 0, 1);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (24, '青海', 24, 291, 0, 267, 0, 167, 152);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (25, '吉林', 18, 40329, 19, 40306, 5, 1, 8);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (26, '贵州', 12, 962, 0, 948, 2, 3, 1);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (27, '西藏', 10, 1463, 0, 1453, 0, 2, 1);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (28, '江西', 9, 1504, 0, 1494, 1, 9, 6);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (29, '湖北', 5, 68444, 25, 63927, 4512, 0, 1);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (30, '河北', 3, 2038, 0, 2028, 7, 261, 339);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (31, '安徽', 3, 1539, 2, 1530, 6, 2, 20);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (32, '宁夏', 2, 225, 0, 223, 0, 10, 19);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (33, '广西', 1, 2348, 0, 2346, 2, 0, 0);
INSERT INTO covid19.province (id, provinceName, nowConfirm, confirm, suspect, heal, dead, highRisk, midRisk) VALUES (34, '澳门', 0, 795, 9, 789, 6, 0, 0);
