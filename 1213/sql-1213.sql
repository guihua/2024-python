-- 创建 city 表
create table city(
  -- 城市ID，自动增长的整数，不为空
  id int NOT NULL AUTO_INCREMENT,
  -- 城市名称，最大长度为50的字符串，不为空
  `name` varchar(50) NOT NULL,
  -- 设置 id 为主键
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 创建 user 表
create table user(
  -- 用户ID，自动增长的整数，不为空
  id int NOT NULL AUTO_INCREMENT,
  -- 用户名称，最大长度为50的字符串，不为空
  `name` varchar(50) NOT NULL,
  -- 用户年龄，整数，不为空
  `age` int NOT NULL,
  -- 设置 id 为主键
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
