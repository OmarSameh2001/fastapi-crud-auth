def itemEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "description":item["description"],
        "date_found":item["date_found"],
        "date_lost":item.get("date_lost"),
        "date_claimed":item["date_claimed"],
        "location_found":item["location_found"],
        "location_claimed":item["location_claimed"],
        "location_lost":item["location_lost"],
        "loser_id":item["loser_id"],
        "claimer_id":item["claimer_id"],
        "founder_id":item["founder_id"],
        "status":item["status"]
    }

def itemsEntity(entity) -> list:
    return [itemEntity(item) for item in entity]