CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);
CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
  FOREIGN KEY(`category_id`) REFERENCES `Categories` (`id`)
);
CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);
CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);



INSERT INTO Categories ('label')
VALUES ('News');
INSERT INTO Tags ('label')
VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');



INSERT INTO Users (
    'first_name',
    'last_name',
    'email',
    'bio',
    'username',
    'password',
    'profile_image_url',
    'created_on',
    'active'
  )
VALUES (
    'Francklin',
    'Parncutt',
    'fparncutt0@wp.com',
    'Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus. Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla.',
    'fparncutt0',
    'BLL1B0q',
    'http://dummyimage.com/145x100.png/dddddd/000000',
    '4/27/2022',
    'true'
  );
INSERT INTO Users (
    'first_name',
    'last_name',
    'email',
    'bio',
    'username',
    'password',
    'profile_image_url',
    'created_on',
    'active'
  )
VALUES (
    'Amandi',
    'Sanson',
    'asanson1@bigcartel.com',
    'Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat.',
    'asanson1',
    '2zsyBD',
    'http://dummyimage.com/145x100.png/dddddd/000000',
    '12/29/2021',
    'true'
  );
INSERT INTO Users (
    'first_name',
    'last_name',
    'email',
    'bio',
    'username',
    'password',
    'profile_image_url',
    'created_on',
    'active'
  )
VALUES (
    'Jerrie',
    'Voas',
    'jvoas2@elpais.com',
    'Donec posuere metus vitae ipsum. Aliquam non mauris. Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.',
    'jvoas2',
    'VS5IwtIt1471',
    'http://dummyimage.com/145x100.png/dddddd/000000',
    '12/3/2021',
    'true'
  );
INSERT INTO Users (
    'first_name',
    'last_name',
    'email',
    'bio',
    'username',
    'password',
    'profile_image_url',
    'created_on',
    'active'
  )
VALUES (
    'Trula',
    'Sancroft',
    'tsancroft3@taobao.com',
    'Donec dapibus. Duis at velit eu est congue elementum. In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.',
    'tsancroft3',
    'fEAwgTU',
    'http://dummyimage.com/145x100.png/dddddd/000000',
    '6/8/2022',
    'true'
  );
INSERT INTO Users (
    'first_name',
    'last_name',
    'email',
    'bio',
    'username',
    'password',
    'profile_image_url',
    'created_on',
    'active'
  )
VALUES (
    'Elena',
    'Grisewood	',
    'egrisewood4@constantcontact.com',
    'Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.',
    'egrisewood4	',
    '3zZbFT',
    'http://dummyimage.com/145x100.png/dddddd/000000',
    '7/28/2022',
    'true'
  );


INSERT INTO Categories ('label')
VALUES('Horror');
INSERT INTO Categories ('label')
VALUES('Fantasy');
INSERT INTO Categories ('label')
VALUES('Anime');
INSERT INTO Categories ('label')
VALUES('Gaming');
INSERT INTO Categories ('label')
VALUES('Crime');
INSERT INTO Categories ('label')
VALUES('Classic');
INSERT INTO Categories ('label')
VALUES('Historical');
INSERT INTO Categories ('label')
VALUES('Fairy Tale');



INSERT INTO Tags ('label')
VALUES('Horror');
INSERT INTO Tags ('label')
VALUES('Fantasy');
INSERT INTO Tags ('label')
VALUES('Anime');
INSERT INTO Tags ('label')
VALUES('Gaming');
INSERT INTO Tags ('label')
VALUES('Classical');
INSERT INTO Tags ('label')
VALUES('Historical');
INSERT INTO Tags ('label')
VALUES('Fairy Tale');


INSERT INTO Reactions ('label', 'image_url')
VALUES('Sad', 'https://pngtree.com/so/sad')
INSERT INTO Reactions ('label', 'image_url')
VALUES('excited', 'https://pngtree.com/so/excited')
INSERT INTO Reactions ('label', 'image_url')
VALUES('angry', 'https://pngtree.com/so/angry')
INSERT INTO Reactions ('label', 'image_url')
VALUES('love', 'https://pngtree.com/so/love')
INSERT INTO Reactions ('label', 'image_url')
VALUES('wink', 'https://pngtree.com/so/wink')

INSERT INTO Posts (
    'id', 
    'user_id', 
    'category_id', 
    'title', 
    'publication_date', 
    'image_url', 
    'content', 
    'approved'
  )
VALUES(
    '2', 
    '1', 
    '5', 
    'Chainsawman', 
    '2022-10-24', 
    'https://upload.wikimedia.org/wikipedia/en/2/24/Chainsawman.jpg',
    'the show is good', 
    'approved'
    )

SELECT
    a.id,
    a.user_id,
    a.category_id,
    a.title,
    a.publication_date,
    a.image_url,
    a.content,
    a.approved,
    u.first_name first_name,
    u.last_name last_name,
    u.email email,
    u.bio bio,
    u.username username,
    u.password password,
    u.profile_image_url profile_image_url,
    u.created_on created_on,
    u.active active,
    c.label category_label
FROM Posts a
JOIN Users u
    ON u.id = a.user_id
JOIN Categories c
    ON c.id = a.category_id

SELECT * FROM Users

UPDATE Users
SET first_name = 'Franklin'
WHERE id =1



INSERT INTO Subscriptions (
    'id', 
    'follower_id', 
    'author_id', 
    'created_on'
  )
VALUES(
    1, 
    2, 
    3, 
    1666641591
  )
INSERT INTO Subscriptions (
    'id', 
    'follower_id', 
    'author_id', 
    'created_on'
  )
VALUES(
    2, 
    4, 
    5, 
    1666641592
  )
INSERT INTO Subscriptions (
    'id', 
    'follower_id', 
    'author_id', 
    'created_on'
  )
VALUES(
    3, 
    6, 
    7, 
    1666641593
  )
INSERT INTO Subscriptions (
    'id', 
    'follower_id', 
    'author_id', 
    'created_on'
  )
VALUES(
    4, 
    8, 
    9,
    1666641594
  )