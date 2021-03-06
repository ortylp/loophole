# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exercise_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import structures_pb2
import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='exercise_stats.proto',
  package='data',
  serialized_pb=_b('\n\x14\x65xercise_stats.proto\x12\x04\x64\x61ta\x1a\x10structures.proto\x1a\x0btypes.proto\"\xde\x01\n\x19PbSwimmingStyleStatistics\x12\x10\n\x08\x64istance\x18\x01 \x02(\x02\x12\x14\n\x0cstroke_count\x18\x02 \x02(\r\x12(\n\x13swimming_time_total\x18\x03 \x01(\x0b\x32\x0b.PbDuration\x12\x19\n\x11\x61verage_heartrate\x18\x04 \x01(\r\x12\x19\n\x11maximum_heartrate\x18\x05 \x01(\r\x12\x15\n\raverage_swolf\x18\x06 \x01(\x02\x12\"\n\rpool_time_min\x18\x07 \x01(\x0b\x32\x0b.PbDuration\"\x9a\x03\n\x14PbSwimmingStatistics\x12\x19\n\x11swimming_distance\x18\x01 \x02(\x02\x12=\n\x14\x66reestyle_statistics\x18\x02 \x01(\x0b\x32\x1f.data.PbSwimmingStyleStatistics\x12>\n\x15\x62\x61\x63kstroke_statistics\x18\x03 \x01(\x0b\x32\x1f.data.PbSwimmingStyleStatistics\x12@\n\x17\x62reaststroke_statistics\x18\x04 \x01(\x0b\x32\x1f.data.PbSwimmingStyleStatistics\x12=\n\x14\x62utterfly_statistics\x18\x05 \x01(\x0b\x32\x1f.data.PbSwimmingStyleStatistics\x12\x1a\n\x12total_stroke_count\x18\x06 \x01(\r\x12\x1f\n\x17number_of_pools_swimmed\x18\x07 \x01(\r\x12*\n\rswimming_pool\x18\x08 \x01(\x0b\x32\x13.PbSwimmingPoolInfo\"J\n\x15PbHeartRateStatistics\x12\x0f\n\x07minimum\x18\x01 \x01(\r\x12\x0f\n\x07\x61verage\x18\x02 \x01(\r\x12\x0f\n\x07maximum\x18\x03 \x01(\r\"5\n\x11PbSpeedStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x02\x12\x0f\n\x07maximum\x18\x02 \x01(\x02\"7\n\x13PbCadenceStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\x12\x0f\n\x07maximum\x18\x02 \x01(\r\"I\n\x14PbAltitudeStatistics\x12\x0f\n\x07minimum\x18\x01 \x01(\x02\x12\x0f\n\x07\x61verage\x18\x02 \x01(\x02\x12\x0f\n\x07maximum\x18\x03 \x01(\x02\"5\n\x11PbPowerStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x05\x12\x0f\n\x07maximum\x18\x02 \x01(\x05\"0\n\x1dPbCyclingEfficiencyStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\"1\n\x1ePbPedalingEfficiencyStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\"(\n\x15PbLRBalanceStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x02\"L\n\x17PbTemperatureStatistics\x12\x0f\n\x07minimum\x18\x01 \x01(\x02\x12\x0f\n\x07\x61verage\x18\x02 \x01(\x02\x12\x0f\n\x07maximum\x18\x03 \x01(\x02\"<\n\x18PbStrideLengthStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\r\x12\x0f\n\x07maximum\x18\x02 \x01(\r\"7\n\x13PbInclineStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x02\x12\x0f\n\x07maximum\x18\x02 \x01(\x02\"7\n\x13PbDeclineStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x02\x12\x0f\n\x07maximum\x18\x02 \x01(\x02\"\'\n\x14PbActivityStatistics\x12\x0f\n\x07\x61verage\x18\x01 \x01(\x02\"\xc9\x04\n\x14PbExerciseStatistics\x12/\n\nheart_rate\x18\x01 \x01(\x0b\x32\x1b.data.PbHeartRateStatistics\x12&\n\x05speed\x18\x02 \x01(\x0b\x32\x17.data.PbSpeedStatistics\x12*\n\x07\x63\x61\x64\x65nce\x18\x03 \x01(\x0b\x32\x19.data.PbCadenceStatistics\x12,\n\x08\x61ltitude\x18\x04 \x01(\x0b\x32\x1a.data.PbAltitudeStatistics\x12&\n\x05power\x18\x05 \x01(\x0b\x32\x17.data.PbPowerStatistics\x12\x37\n\x12left_right_balance\x18\x06 \x01(\x0b\x32\x1b.data.PbLRBalanceStatistics\x12\x32\n\x0btemperature\x18\x07 \x01(\x0b\x32\x1d.data.PbTemperatureStatistics\x12,\n\x08\x61\x63tivity\x18\x08 \x01(\x0b\x32\x1a.data.PbActivityStatistics\x12\x35\n\rstride_length\x18\t \x01(\x0b\x32\x1e.data.PbStrideLengthStatistics\x12*\n\x07incline\x18\n \x01(\x0b\x32\x19.data.PbInclineStatistics\x12*\n\x07\x64\x65\x63line\x18\x0b \x01(\x0b\x32\x19.data.PbDeclineStatistics\x12,\n\x08swimming\x18\x0c \x01(\x0b\x32\x1a.data.PbSwimmingStatistics')
  ,
  dependencies=[structures_pb2.DESCRIPTOR,types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBSWIMMINGSTYLESTATISTICS = _descriptor.Descriptor(
  name='PbSwimmingStyleStatistics',
  full_name='data.PbSwimmingStyleStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='distance', full_name='data.PbSwimmingStyleStatistics.distance', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stroke_count', full_name='data.PbSwimmingStyleStatistics.stroke_count', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swimming_time_total', full_name='data.PbSwimmingStyleStatistics.swimming_time_total', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_heartrate', full_name='data.PbSwimmingStyleStatistics.average_heartrate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_heartrate', full_name='data.PbSwimmingStyleStatistics.maximum_heartrate', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_swolf', full_name='data.PbSwimmingStyleStatistics.average_swolf', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pool_time_min', full_name='data.PbSwimmingStyleStatistics.pool_time_min', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=62,
  serialized_end=284,
)


_PBSWIMMINGSTATISTICS = _descriptor.Descriptor(
  name='PbSwimmingStatistics',
  full_name='data.PbSwimmingStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swimming_distance', full_name='data.PbSwimmingStatistics.swimming_distance', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='freestyle_statistics', full_name='data.PbSwimmingStatistics.freestyle_statistics', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backstroke_statistics', full_name='data.PbSwimmingStatistics.backstroke_statistics', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='breaststroke_statistics', full_name='data.PbSwimmingStatistics.breaststroke_statistics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='butterfly_statistics', full_name='data.PbSwimmingStatistics.butterfly_statistics', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_stroke_count', full_name='data.PbSwimmingStatistics.total_stroke_count', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_pools_swimmed', full_name='data.PbSwimmingStatistics.number_of_pools_swimmed', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swimming_pool', full_name='data.PbSwimmingStatistics.swimming_pool', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=287,
  serialized_end=697,
)


_PBHEARTRATESTATISTICS = _descriptor.Descriptor(
  name='PbHeartRateStatistics',
  full_name='data.PbHeartRateStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum', full_name='data.PbHeartRateStatistics.minimum', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbHeartRateStatistics.average', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbHeartRateStatistics.maximum', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=699,
  serialized_end=773,
)


_PBSPEEDSTATISTICS = _descriptor.Descriptor(
  name='PbSpeedStatistics',
  full_name='data.PbSpeedStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbSpeedStatistics.average', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbSpeedStatistics.maximum', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=775,
  serialized_end=828,
)


_PBCADENCESTATISTICS = _descriptor.Descriptor(
  name='PbCadenceStatistics',
  full_name='data.PbCadenceStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbCadenceStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbCadenceStatistics.maximum', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=830,
  serialized_end=885,
)


_PBALTITUDESTATISTICS = _descriptor.Descriptor(
  name='PbAltitudeStatistics',
  full_name='data.PbAltitudeStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum', full_name='data.PbAltitudeStatistics.minimum', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbAltitudeStatistics.average', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbAltitudeStatistics.maximum', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=887,
  serialized_end=960,
)


_PBPOWERSTATISTICS = _descriptor.Descriptor(
  name='PbPowerStatistics',
  full_name='data.PbPowerStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbPowerStatistics.average', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbPowerStatistics.maximum', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=962,
  serialized_end=1015,
)


_PBCYCLINGEFFICIENCYSTATISTICS = _descriptor.Descriptor(
  name='PbCyclingEfficiencyStatistics',
  full_name='data.PbCyclingEfficiencyStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbCyclingEfficiencyStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=1017,
  serialized_end=1065,
)


_PBPEDALINGEFFICIENCYSTATISTICS = _descriptor.Descriptor(
  name='PbPedalingEfficiencyStatistics',
  full_name='data.PbPedalingEfficiencyStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbPedalingEfficiencyStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=1067,
  serialized_end=1116,
)


_PBLRBALANCESTATISTICS = _descriptor.Descriptor(
  name='PbLRBalanceStatistics',
  full_name='data.PbLRBalanceStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbLRBalanceStatistics.average', index=0,
      number=1, type=2, cpp_type=6, label=1,
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
  serialized_start=1118,
  serialized_end=1158,
)


_PBTEMPERATURESTATISTICS = _descriptor.Descriptor(
  name='PbTemperatureStatistics',
  full_name='data.PbTemperatureStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum', full_name='data.PbTemperatureStatistics.minimum', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbTemperatureStatistics.average', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbTemperatureStatistics.maximum', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=1160,
  serialized_end=1236,
)


_PBSTRIDELENGTHSTATISTICS = _descriptor.Descriptor(
  name='PbStrideLengthStatistics',
  full_name='data.PbStrideLengthStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbStrideLengthStatistics.average', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbStrideLengthStatistics.maximum', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=1238,
  serialized_end=1298,
)


_PBINCLINESTATISTICS = _descriptor.Descriptor(
  name='PbInclineStatistics',
  full_name='data.PbInclineStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbInclineStatistics.average', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbInclineStatistics.maximum', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=1300,
  serialized_end=1355,
)


_PBDECLINESTATISTICS = _descriptor.Descriptor(
  name='PbDeclineStatistics',
  full_name='data.PbDeclineStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbDeclineStatistics.average', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='data.PbDeclineStatistics.maximum', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=1357,
  serialized_end=1412,
)


_PBACTIVITYSTATISTICS = _descriptor.Descriptor(
  name='PbActivityStatistics',
  full_name='data.PbActivityStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average', full_name='data.PbActivityStatistics.average', index=0,
      number=1, type=2, cpp_type=6, label=1,
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
  serialized_start=1414,
  serialized_end=1453,
)


_PBEXERCISESTATISTICS = _descriptor.Descriptor(
  name='PbExerciseStatistics',
  full_name='data.PbExerciseStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heart_rate', full_name='data.PbExerciseStatistics.heart_rate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='data.PbExerciseStatistics.speed', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cadence', full_name='data.PbExerciseStatistics.cadence', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='data.PbExerciseStatistics.altitude', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='data.PbExerciseStatistics.power', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_right_balance', full_name='data.PbExerciseStatistics.left_right_balance', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='data.PbExerciseStatistics.temperature', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity', full_name='data.PbExerciseStatistics.activity', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stride_length', full_name='data.PbExerciseStatistics.stride_length', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incline', full_name='data.PbExerciseStatistics.incline', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decline', full_name='data.PbExerciseStatistics.decline', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swimming', full_name='data.PbExerciseStatistics.swimming', index=11,
      number=12, type=11, cpp_type=10, label=1,
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
  serialized_start=1456,
  serialized_end=2041,
)

_PBSWIMMINGSTYLESTATISTICS.fields_by_name['swimming_time_total'].message_type = types_pb2._PBDURATION
_PBSWIMMINGSTYLESTATISTICS.fields_by_name['pool_time_min'].message_type = types_pb2._PBDURATION
_PBSWIMMINGSTATISTICS.fields_by_name['freestyle_statistics'].message_type = _PBSWIMMINGSTYLESTATISTICS
_PBSWIMMINGSTATISTICS.fields_by_name['backstroke_statistics'].message_type = _PBSWIMMINGSTYLESTATISTICS
_PBSWIMMINGSTATISTICS.fields_by_name['breaststroke_statistics'].message_type = _PBSWIMMINGSTYLESTATISTICS
_PBSWIMMINGSTATISTICS.fields_by_name['butterfly_statistics'].message_type = _PBSWIMMINGSTYLESTATISTICS
_PBSWIMMINGSTATISTICS.fields_by_name['swimming_pool'].message_type = structures_pb2._PBSWIMMINGPOOLINFO
_PBEXERCISESTATISTICS.fields_by_name['heart_rate'].message_type = _PBHEARTRATESTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['speed'].message_type = _PBSPEEDSTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['cadence'].message_type = _PBCADENCESTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['altitude'].message_type = _PBALTITUDESTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['power'].message_type = _PBPOWERSTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['left_right_balance'].message_type = _PBLRBALANCESTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['temperature'].message_type = _PBTEMPERATURESTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['activity'].message_type = _PBACTIVITYSTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['stride_length'].message_type = _PBSTRIDELENGTHSTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['incline'].message_type = _PBINCLINESTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['decline'].message_type = _PBDECLINESTATISTICS
_PBEXERCISESTATISTICS.fields_by_name['swimming'].message_type = _PBSWIMMINGSTATISTICS
DESCRIPTOR.message_types_by_name['PbSwimmingStyleStatistics'] = _PBSWIMMINGSTYLESTATISTICS
DESCRIPTOR.message_types_by_name['PbSwimmingStatistics'] = _PBSWIMMINGSTATISTICS
DESCRIPTOR.message_types_by_name['PbHeartRateStatistics'] = _PBHEARTRATESTATISTICS
DESCRIPTOR.message_types_by_name['PbSpeedStatistics'] = _PBSPEEDSTATISTICS
DESCRIPTOR.message_types_by_name['PbCadenceStatistics'] = _PBCADENCESTATISTICS
DESCRIPTOR.message_types_by_name['PbAltitudeStatistics'] = _PBALTITUDESTATISTICS
DESCRIPTOR.message_types_by_name['PbPowerStatistics'] = _PBPOWERSTATISTICS
DESCRIPTOR.message_types_by_name['PbCyclingEfficiencyStatistics'] = _PBCYCLINGEFFICIENCYSTATISTICS
DESCRIPTOR.message_types_by_name['PbPedalingEfficiencyStatistics'] = _PBPEDALINGEFFICIENCYSTATISTICS
DESCRIPTOR.message_types_by_name['PbLRBalanceStatistics'] = _PBLRBALANCESTATISTICS
DESCRIPTOR.message_types_by_name['PbTemperatureStatistics'] = _PBTEMPERATURESTATISTICS
DESCRIPTOR.message_types_by_name['PbStrideLengthStatistics'] = _PBSTRIDELENGTHSTATISTICS
DESCRIPTOR.message_types_by_name['PbInclineStatistics'] = _PBINCLINESTATISTICS
DESCRIPTOR.message_types_by_name['PbDeclineStatistics'] = _PBDECLINESTATISTICS
DESCRIPTOR.message_types_by_name['PbActivityStatistics'] = _PBACTIVITYSTATISTICS
DESCRIPTOR.message_types_by_name['PbExerciseStatistics'] = _PBEXERCISESTATISTICS

PbSwimmingStyleStatistics = _reflection.GeneratedProtocolMessageType('PbSwimmingStyleStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBSWIMMINGSTYLESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSwimmingStyleStatistics)
  ))
_sym_db.RegisterMessage(PbSwimmingStyleStatistics)

PbSwimmingStatistics = _reflection.GeneratedProtocolMessageType('PbSwimmingStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBSWIMMINGSTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSwimmingStatistics)
  ))
_sym_db.RegisterMessage(PbSwimmingStatistics)

PbHeartRateStatistics = _reflection.GeneratedProtocolMessageType('PbHeartRateStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBHEARTRATESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbHeartRateStatistics)
  ))
_sym_db.RegisterMessage(PbHeartRateStatistics)

PbSpeedStatistics = _reflection.GeneratedProtocolMessageType('PbSpeedStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBSPEEDSTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSpeedStatistics)
  ))
_sym_db.RegisterMessage(PbSpeedStatistics)

PbCadenceStatistics = _reflection.GeneratedProtocolMessageType('PbCadenceStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBCADENCESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbCadenceStatistics)
  ))
_sym_db.RegisterMessage(PbCadenceStatistics)

PbAltitudeStatistics = _reflection.GeneratedProtocolMessageType('PbAltitudeStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBALTITUDESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbAltitudeStatistics)
  ))
_sym_db.RegisterMessage(PbAltitudeStatistics)

PbPowerStatistics = _reflection.GeneratedProtocolMessageType('PbPowerStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBPOWERSTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbPowerStatistics)
  ))
_sym_db.RegisterMessage(PbPowerStatistics)

PbCyclingEfficiencyStatistics = _reflection.GeneratedProtocolMessageType('PbCyclingEfficiencyStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBCYCLINGEFFICIENCYSTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbCyclingEfficiencyStatistics)
  ))
_sym_db.RegisterMessage(PbCyclingEfficiencyStatistics)

PbPedalingEfficiencyStatistics = _reflection.GeneratedProtocolMessageType('PbPedalingEfficiencyStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBPEDALINGEFFICIENCYSTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbPedalingEfficiencyStatistics)
  ))
_sym_db.RegisterMessage(PbPedalingEfficiencyStatistics)

PbLRBalanceStatistics = _reflection.GeneratedProtocolMessageType('PbLRBalanceStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBLRBALANCESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbLRBalanceStatistics)
  ))
_sym_db.RegisterMessage(PbLRBalanceStatistics)

PbTemperatureStatistics = _reflection.GeneratedProtocolMessageType('PbTemperatureStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBTEMPERATURESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbTemperatureStatistics)
  ))
_sym_db.RegisterMessage(PbTemperatureStatistics)

PbStrideLengthStatistics = _reflection.GeneratedProtocolMessageType('PbStrideLengthStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBSTRIDELENGTHSTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbStrideLengthStatistics)
  ))
_sym_db.RegisterMessage(PbStrideLengthStatistics)

PbInclineStatistics = _reflection.GeneratedProtocolMessageType('PbInclineStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBINCLINESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbInclineStatistics)
  ))
_sym_db.RegisterMessage(PbInclineStatistics)

PbDeclineStatistics = _reflection.GeneratedProtocolMessageType('PbDeclineStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBDECLINESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbDeclineStatistics)
  ))
_sym_db.RegisterMessage(PbDeclineStatistics)

PbActivityStatistics = _reflection.GeneratedProtocolMessageType('PbActivityStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBACTIVITYSTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbActivityStatistics)
  ))
_sym_db.RegisterMessage(PbActivityStatistics)

PbExerciseStatistics = _reflection.GeneratedProtocolMessageType('PbExerciseStatistics', (_message.Message,), dict(
  DESCRIPTOR = _PBEXERCISESTATISTICS,
  __module__ = 'exercise_stats_pb2'
  # @@protoc_insertion_point(class_scope:data.PbExerciseStatistics)
  ))
_sym_db.RegisterMessage(PbExerciseStatistics)


# @@protoc_insertion_point(module_scope)
