DROP TABLE HOME CASCADE CONSTRAINTS;
DROP TABLE CANADIAN CASCADE CONSTRAINTS;
DROP TABLE PET CASCADE CONSTRAINTS;
DROP TABLE VEHICLE CASCADE CONSTRAINTS;
DROP TABLE RELATIONSHIP CASCADE CONSTRAINTS;

CREATE TABLE HOME (
      HID             INTEGER     PRIMARY KEY,
      HTYPE           VARCHAR(50) NOT NULL,
      HCITY           VARCHAR(50) NOT NULL,
      HSTREET_NAME    VARCHAR(50) NOT NULL,
      HSTREET_NUMBER  INTEGER     NOT NULL,
      HAPT_NUMBER     INTEGER,
      HPOSTAL_CODE    VARCHAR(50) NOT NULL
);
CREATE TABLE CANADIAN (
      CID           INTEGER     PRIMARY KEY,
      CFIRST_NAME   VARCHAR(50) NOT NULL,
      CFAMILY_NAME  VARCHAR(50) NOT NULL,
      CAGE          INTEGER,
      CAN_HID       INTEGER     NOT NULL
);
CREATE TABLE PET (
      PID       INTEGER     PRIMARY KEY,
      PNAME     VARCHAR(50) Not Null,
      PSPECIES  VARCHAR(50) Not Null,
      PAGE      INTEGER,
      PET_CID   INTEGER     NOT NULL
);
CREATE TABLE VEHICLE (
      VTYPE               VARCHAR(50) Not Null,
      VSUITABLE_IN_SNOW   NUMBER(1)   Not Null,
      VAGE                INTEGER,
      VEH_CID             INTEGER     PRIMARY KEY REFERENCES CANADIAN(CID)
);

CREATE TABLE RELATIONSHIP (
      RID       INTEGER     PRIMARY KEY,      
      CTYPE     VARCHAR(50) NOT NULL,
      R_CID_1   INTEGER     NOT NULL,
      R_CID_2   INTEGER     NOT NULL
);

ALTER TABLE CANADIAN ADD (
      CONSTRAINT FK_CAN_HID FOREIGN KEY (CAN_HID) REFERENCES HOME(HID)
);

ALTER TABLE PET ADD (
      CONSTRAINT FK_PET_CID FOREIGN KEY (PET_CID) REFERENCES CANADIAN(CID)
);

ALTER TABLE RELATIONSHIP ADD (
      CONSTRAINT FK_REL_CID_1 FOREIGN KEY (R_CID_1) REFERENCES CANADIAN(CID),
      CONSTRAINT FK_REL_CID_2 FOREIGN KEY (R_CID_2) REFERENCES CANADIAN(CID)
);