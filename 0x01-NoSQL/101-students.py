#!/usr/bin/env python3
'''
Write a Python function that returns all students sorted by average score:

Prototype: def top_students(mongo_collection):
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returns with key = averageScore
'''


def top_students(mongo_collection):
    '''Returns all students sorted by average score'''
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    top_students = list(mongo_collection.aggregate(pipeline))
    for student in top_students:
        student["_id"] = str(student["_id"])  # Convert ObjectId to string
    return top_students
