-- Insert 5 Users
INSERT INTO Users (Name, Email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com'),
('Diana Prince', 'diana@example.com'),
('Ethan Hunt', 'ethan@example.com');

-- Insert 10 Transactions for each User
-- User 1 (Alice)
INSERT INTO Transactions (UserId, Amount, Date) VALUES
(1, 100.50, GETDATE()), (1, 200.75, GETDATE()), (1, 50.00, GETDATE()),
(1, 300.25, GETDATE()), (1, 400.00, GETDATE()), (1, 150.10, GETDATE()),
(1, 220.40, GETDATE()), (1, 330.60, GETDATE()), (1, 500.00, GETDATE()),
(1, 75.25, GETDATE());

-- User 2 (Bob)
INSERT INTO Transactions (UserId, Amount, Date) VALUES
(2, 120.00, GETDATE()), (2, 250.50, GETDATE()), (2, 80.75, GETDATE()),
(2, 310.00, GETDATE()), (2, 450.25, GETDATE()), (2, 95.00, GETDATE()),
(2, 210.40, GETDATE()), (2, 330.10, GETDATE()), (2, 600.00, GETDATE()),
(2, 70.25, GETDATE());

-- User 3 (Charlie)
INSERT INTO Transactions (UserId, Amount, Date) VALUES
(3, 130.00, GETDATE()), (3, 240.50, GETDATE()), (3, 90.75, GETDATE()),
(3, 320.00, GETDATE()), (3, 410.25, GETDATE()), (3, 85.00, GETDATE()),
(3, 215.40, GETDATE()), (3, 335.10, GETDATE()), (3, 620.00, GETDATE()),
(3, 65.25, GETDATE());

-- User 4 (Diana)
INSERT INTO Transactions (UserId, Amount, Date) VALUES
(4, 140.00, GETDATE()), (4, 260.50, GETDATE()), (4, 95.75, GETDATE()),
(4, 330.00, GETDATE()), (4, 420.25, GETDATE()), (4, 105.00, GETDATE()),
(4, 225.40, GETDATE()), (4, 345.10, GETDATE()), (4, 640.00, GETDATE()),
(4, 85.25, GETDATE());

-- User 5 (Ethan)
INSERT INTO Transactions (UserId, Amount, Date) VALUES
(5, 150.00, GETDATE()), (5, 270.50, GETDATE()), (5, 100.75, GETDATE()),
(5, 340.00, GETDATE()), (5, 430.25, GETDATE()), (5, 115.00, GETDATE()),
(5, 235.40, GETDATE()), (5, 355.10, GETDATE()), (5, 660.00, GETDATE()),
(5, 95.25, GETDATE());
