BEGIN BATCH

INSERT INTO citizix.dog (id, breedId, colorId)
VALUES(2, 2, 2);

INSERT INTO citizix.dog (id, breedId, colorId)
VALUES(3, 3, 3);

INSERT INTO citizix.dog (id, breedId, colorId)
VALUES(4, 4, 4);

DELETE FROM citizix.dog WHERE id = 2;

UPDATE citizix.dog SET breedId=5 WHERE id = 2;

APPLY BATCH;
