# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: swimming_samples.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='swimming_samples.proto',
  package='data',
  serialized_pb=_b('\n\x16swimming_samples.proto\x12\x04\x64\x61ta\x1a\x0btypes.proto\"X\n\x15PbSwimmingStyleChange\x12\x1f\n\x05style\x18\x01 \x02(\x0e\x32\x10.PbSwimmingStyle\x12\x1e\n\ttimestamp\x18\x02 \x02(\x0b\x32\x0b.PbDuration\"\x8a\x01\n\x14PbSwimmingPoolMetric\x12!\n\x0cstart_offset\x18\x01 \x02(\x0b\x32\x0b.PbDuration\x12\x1d\n\x08\x64uration\x18\x02 \x02(\x0b\x32\x0b.PbDuration\x12\x1f\n\x05style\x18\x03 \x01(\x0e\x32\x10.PbSwimmingStyle\x12\x0f\n\x07strokes\x18\x04 \x01(\r\"e\n\x11PbSwimmingSamples\x12\x1f\n\x05start\x18\x01 \x02(\x0b\x32\x10.PbLocalDateTime\x12/\n\x0bpool_metric\x18\x03 \x03(\x0b\x32\x1a.data.PbSwimmingPoolMetric')
  ,
  dependencies=[types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBSWIMMINGSTYLECHANGE = _descriptor.Descriptor(
  name='PbSwimmingStyleChange',
  full_name='data.PbSwimmingStyleChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='style', full_name='data.PbSwimmingStyleChange.style', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='data.PbSwimmingStyleChange.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=133,
)


_PBSWIMMINGPOOLMETRIC = _descriptor.Descriptor(
  name='PbSwimmingPoolMetric',
  full_name='data.PbSwimmingPoolMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_offset', full_name='data.PbSwimmingPoolMetric.start_offset', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='data.PbSwimmingPoolMetric.duration', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='style', full_name='data.PbSwimmingPoolMetric.style', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strokes', full_name='data.PbSwimmingPoolMetric.strokes', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=274,
)


_PBSWIMMINGSAMPLES = _descriptor.Descriptor(
  name='PbSwimmingSamples',
  full_name='data.PbSwimmingSamples',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='data.PbSwimmingSamples.start', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pool_metric', full_name='data.PbSwimmingSamples.pool_metric', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=377,
)

_PBSWIMMINGSTYLECHANGE.fields_by_name['style'].enum_type = types_pb2._PBSWIMMINGSTYLE
_PBSWIMMINGSTYLECHANGE.fields_by_name['timestamp'].message_type = types_pb2._PBDURATION
_PBSWIMMINGPOOLMETRIC.fields_by_name['start_offset'].message_type = types_pb2._PBDURATION
_PBSWIMMINGPOOLMETRIC.fields_by_name['duration'].message_type = types_pb2._PBDURATION
_PBSWIMMINGPOOLMETRIC.fields_by_name['style'].enum_type = types_pb2._PBSWIMMINGSTYLE
_PBSWIMMINGSAMPLES.fields_by_name['start'].message_type = types_pb2._PBLOCALDATETIME
_PBSWIMMINGSAMPLES.fields_by_name['pool_metric'].message_type = _PBSWIMMINGPOOLMETRIC
DESCRIPTOR.message_types_by_name['PbSwimmingStyleChange'] = _PBSWIMMINGSTYLECHANGE
DESCRIPTOR.message_types_by_name['PbSwimmingPoolMetric'] = _PBSWIMMINGPOOLMETRIC
DESCRIPTOR.message_types_by_name['PbSwimmingSamples'] = _PBSWIMMINGSAMPLES

PbSwimmingStyleChange = _reflection.GeneratedProtocolMessageType('PbSwimmingStyleChange', (_message.Message,), dict(
  DESCRIPTOR = _PBSWIMMINGSTYLECHANGE,
  __module__ = 'swimming_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSwimmingStyleChange)
  ))
_sym_db.RegisterMessage(PbSwimmingStyleChange)

PbSwimmingPoolMetric = _reflection.GeneratedProtocolMessageType('PbSwimmingPoolMetric', (_message.Message,), dict(
  DESCRIPTOR = _PBSWIMMINGPOOLMETRIC,
  __module__ = 'swimming_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSwimmingPoolMetric)
  ))
_sym_db.RegisterMessage(PbSwimmingPoolMetric)

PbSwimmingSamples = _reflection.GeneratedProtocolMessageType('PbSwimmingSamples', (_message.Message,), dict(
  DESCRIPTOR = _PBSWIMMINGSAMPLES,
  __module__ = 'swimming_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSwimmingSamples)
  ))
_sym_db.RegisterMessage(PbSwimmingSamples)


# @@protoc_insertion_point(module_scope)
