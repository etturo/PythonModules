#!/usr/bin/env python3
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class ProcessingPipeline(ABC):
    def process(self, data: Any) -> Any:

class InputStage(ProcessingPipeline):

class TransformStage(ProcessingPipeline):

class OutputStage(ProcessingPipeline):