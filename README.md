# 💻 CodersCave Internship Projects

> Python programming projects, automation scripts, and task assignments completed during the CodersCave internship program.

![Python](https://img.shields.io/badge/Python-Projects-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## ⭐ Star Schema (Automation Task Execution Model)

```
                            +-----------------------------------+
                            |           Dim_TaskType            |
                            +-----------------------------------+
                            | Task_Type_Key (PK)                |
                            | Category_Name                     |
                            +-----------------+-----------------+
                                              | 1
                                              |
                                              | N
+-----------------------+   +-----------------+-----------------+   +-----------------------+
|  Dim_Calendar         | 1 |        Fact_TaskExecution         | 1 |  Dim_Script           |
+-----------------------+---+-----------------------------------+---+-----------------------+
| DateKey (PK)          | N | Execution_Key (PK)                | N | Script_Key (PK)       |
| FullDate              |   | DateKey (FK)                      |   | Script_Name           |
+-----------------------+   | Task_Type_Key (FK)                |   | Language (Python)     |
                            | Script_Key (FK)                   |   +-----------------------+
                            | Files_Processed_Count (Measure)   |
                            | Execution_Time_Ms (Measure)       |
                            +-----------------------------------+
```
