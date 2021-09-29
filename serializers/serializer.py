import json
from dataclasses import is_dataclass
from datetime import date, datetime
from typing import Any, Dict, List, Union
from uuid import UUID


class Serializer:

    def __init__(self, obj: Any) -> None:
        self.__obj = obj

        if isinstance(obj, list):
            json_classes = []
            for obj_list in obj:
                json_class = self.__convert_dataclass_to_json(obj_list)
                json_classes.append(json_class)

            self.__obj = obj
            self.__json = json_classes
        elif isinstance(obj, dict):
            self.__json = obj
            self.__obj = self.__convert_json_to_dataclass(obj)
        elif is_dataclass(obj):
            self.__obj = obj
            self.__json = self.__convert_dataclass_to_json(obj)
        else:
            raise ValueError

    def serialize(self) -> Union[List, Dict]:
        return json.dumps(self.__json)

    def deserialize(self) -> Any:
        return self.__obj

    def __convert_dataclass_to_json(self, obj: Any) -> Dict:
        if not is_dataclass(obj):
            raise ValueError

        json_class = {}

        for attr in self.read_fields:
            if hasattr(obj, attr):
                attr_value = getattr(obj, attr)
                if isinstance(attr_value, date):
                    json_class[attr] = attr_value.strftime('%Y-%m-%d')
                elif isinstance(attr_value, datetime):
                    json_class[attr] = attr_value.strftime("%Y-%m-%d %H:%M:%S.%f")
                elif isinstance(attr_value, UUID):
                    json_class[attr] = str(attr_value)
                elif is_dataclass(attr_value) and not isinstance(attr_value, type):
                    json_class[attr] = getattr(attr_value , 'id')
                else:
                    json_class[attr] = attr_value

        return json_class

    def __convert_json_to_dataclass(self, obj: Dict) -> Any:
        if not isinstance(obj, dict):
            raise ValueError

        class_json = {}
        for attr in self.write_fields:
            if attr in obj:
                attr_value = obj[attr]
                try:
                    class_json[attr] = UUID(attr_value)
                    continue
                except:
                    pass

                try:
                    class_json[attr] = datetime.strptime(attr_value, '%Y-%m-%d %H:%M:%S.%f')
                    continue
                except:
                    pass

                try:
                    class_json[attr] = datetime.strptime(attr_value, '%Y-%m-%d').date()
                    continue
                except:
                    pass

                class_json[attr] = attr_value

        return self.cls(**class_json)
