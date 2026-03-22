-- Create Users table
CREATE TABLE Users (
    UserId INT IDENTITY(1,1) PRIMARY KEY,   -- Auto-increment PK
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(255) UNIQUE NOT NULL
);

-- Create Transactions table
CREATE TABLE Transactions (
    Id INT IDENTITY(1,1) PRIMARY KEY,       -- Auto-increment PK
    UserId INT NOT NULL,                    -- FK to Users
    Amount DECIMAL(18,2) NOT NULL,          -- Decimal with precision
    Date DATETIME NOT NULL DEFAULT GETDATE(), -- Defaults to current date/time
    CONSTRAINT FK_Transactions_Users FOREIGN KEY (UserId)
        REFERENCES Users(UserId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
