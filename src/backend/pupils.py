from typing import Dict, List, Optional, Type, TypeVar

import json
from pydantic import Field, BaseModel, model_serializer

from openai_session_handler.models.beta import register_composite_fields_and_type
from openai_session_handler.models.threads.basethread import BaseThread
from openai_session_handler.models.assistants.baseassistant import BaseAssistant

from openai_session_handler.models.messages.basemessage import BaseMessage
#from openai_session_handler.models.runs.baserun import BaseRun

T = TypeVar('T', bound='Pupil')

class ReadingTutor(BaseAssistant):
    """ PLACE HOLDER FOR ASSISTANT INSTRUCTIONS """
    provider:Optional[str] = Field(default="")
    real_model:Optional[str] = Field(default="")


    @classmethod
    def create(cls: type[T], **kwargs) -> T:
        if kwargs['real_model'] != None:
            kwargs['model'] = kwargs['real_model']

        return super().create(**kwargs)        

    
    def update(self, **kwargs):
        if kwargs['real_model'] != None:
            kwargs['model'] = kwargs['real_model']

        return super().update(**kwargs)
    


class BasePupil(BaseModel):
    pupil_id:str = Field(...)

    @model_serializer
    def compact_ser(self) -> str:
        return json.dumps([self.pupil_id])

    @staticmethod
    def compact_deser(string: str) -> Dict :
        list_fields = json.loads(string)
        return {
            'pupil_id': list_fields[0]
        }


class PupilTracker(BaseAssistant):
    pupils_1:Optional[str] = Field(default="")
    pupils_2:Optional[str] = Field(default="")
    pupils_3:Optional[str] = Field(default="")
    pupils_4:Optional[str] = Field(default="")
    pupils_5:Optional[str] = Field(default="")
    pupils_6:Optional[str] = Field(default="")
    pupils_7:Optional[str] = Field(default="")
    pupils_8:Optional[str] = Field(default="")

    register_composite_fields_and_type("pupils", ["pupils_1", "pupils_2", "pupils_3", "pupils_4","pupils_5", "pupils_6", "pupils_7", "pupils_8" ], BasePupil)

    @property
    def pupils(self) -> List[BasePupil]:
        return self.get_composite_field('pupils')
    
    def add_pupil(self, pupil_id):
        pupils = self.pupils

        pupil_instance = BasePupil(pupil_id=pupil_id)
        pupils.append(pupil_instance)
        self.save_composite_field('pupils', pupils)

    def delete_pupil(self, pupil_id):
        pupils = self.pupils
        pupils_updated = []

        for pupil in pupils:
            if pupil.pupil_id == pupil_id:
                pass
            else: 
                pupils_updated.append(pupil)

        self.save_composite_field('pupils', pupils_updated)

class Pupil(BaseThread): 
    pupil_name:Optional[str] = Field(default="")
    pupil_password:Optional[str] = Field(default="1234")
    pupil_role:Optional[str] = Field(default="user")

    @classmethod
    def create(cls:Type[T], **kwargs) -> T:

        if len(PupilTracker.list()) == 0:
            pupil_tracker = PupilTracker.create()
        else: 
            pupil_tracker = PupilTracker.list()[0]
    
        pupil = super().create(**kwargs)
        print(pupil)

        pupil_tracker.add_pupil(pupil_id=pupil.id)

    @classmethod
    def delete(cls:Type[T], pupil_id):
        if len(PupilTracker.list()) == 0:
            pass
        else: 
            pupil_tracker = PupilTracker.list()[0]
            pupil_tracker.delete_pupil(pupil_id=pupil_id)
            return super().delete(thread_id=pupil_id)
    
    @classmethod
    def list(cls:Type[T]):
        if len(PupilTracker.list()) == 0:
            return []
        else:            
            return PupilTracker.list()[0].pupils
        
    @classmethod
    def retrieve(cls: type[T], pupil_id) -> T:
        return super().retrieve(pupil_id)


class PupilMessage(BaseMessage): 
    pass