# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo.proto',
  package='echo',
  syntax='proto3',
  serialized_options=_b('Z\004echo'),
  serialized_pb=_b('\n\necho.proto\x12\x04\x65\x63ho\"0\n\rSimpleMessage\x12\x0e\n\x06msg_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t28\n\x04\x45\x63ho\x12\x30\n\x02Hi\x12\x13.echo.SimpleMessage\x1a\x13.echo.SimpleMessage\"\x00\x42\x06Z\x04\x65\x63hob\x06proto3')
)




_SIMPLEMESSAGE = _descriptor.Descriptor(
  name='SimpleMessage',
  full_name='echo.SimpleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='echo.SimpleMessage.msg_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='echo.SimpleMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['SimpleMessage'] = _SIMPLEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleMessage = _reflection.GeneratedProtocolMessageType('SimpleMessage', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEMESSAGE,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.SimpleMessage)
  })
_sym_db.RegisterMessage(SimpleMessage)


DESCRIPTOR._options = None

_ECHO = _descriptor.ServiceDescriptor(
  name='Echo',
  full_name='echo.Echo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=70,
  serialized_end=126,
  methods=[
  _descriptor.MethodDescriptor(
    name='Hi',
    full_name='echo.Echo.Hi',
    index=0,
    containing_service=None,
    input_type=_SIMPLEMESSAGE,
    output_type=_SIMPLEMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHO)

DESCRIPTOR.services_by_name['Echo'] = _ECHO

# @@protoc_insertion_point(module_scope)
