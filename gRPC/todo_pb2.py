# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x04todo\x1a\x1bgoogle/protobuf/empty.proto\"\x07\n\x05\x45mpty\" \n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04task\x18\x02 \x01(\t\"%\n\x08TaskList\x12\x19\n\x05tasks\x18\x01 \x03(\x0b\x32\n.todo.Task2\xb3\x01\n\x0bTodoService\x12$\n\nCreateTask\x12\n.todo.Task\x1a\n.todo.Task\x12$\n\nUpdateTask\x12\n.todo.Task\x1a\n.todo.Task\x12$\n\nDeleteTask\x12\n.todo.Task\x1a\n.todo.Task\x12\x32\n\x08GetTasks\x12\x16.google.protobuf.Empty\x1a\x0e.todo.TaskListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=49
  _globals['_EMPTY']._serialized_end=56
  _globals['_TASK']._serialized_start=58
  _globals['_TASK']._serialized_end=90
  _globals['_TASKLIST']._serialized_start=92
  _globals['_TASKLIST']._serialized_end=129
  _globals['_TODOSERVICE']._serialized_start=132
  _globals['_TODOSERVICE']._serialized_end=311
# @@protoc_insertion_point(module_scope)
