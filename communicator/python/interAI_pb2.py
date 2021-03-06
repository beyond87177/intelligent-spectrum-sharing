# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interAI.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='interAI.proto',
  package='aiCommunicator',
  syntax='proto3',
  serialized_pb=_b('\n\rinterAI.proto\x12\x0e\x61iCommunicator\"B\n\x08Location\x12\x11\n\tlongitude\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\televation\x18\x03 \x01(\x01\"g\n\rInternalVoxel\x12\x10\n\x08timeslot\x18\x01 \x01(\r\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\r\x12\x0b\n\x03\x64st\x18\x03 \x01(\x04\x12\x15\n\rvaliditystart\x18\x04 \x01(\x04\x12\x0f\n\x07tx_gain\x18\x05 \x01(\r\"A\n\x0fTXSlotAllocated\x12\x0b\n\x03\x64st\x18\x01 \x01(\x04\x12\x10\n\x08timeslot\x18\x02 \x01(\r\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\r\"2\n\rTXSlotRemoved\x12\x10\n\x08timeslot\x18\x01 \x01(\r\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\r\"*\n\rTXGainChanged\x12\x0b\n\x03\x64st\x18\x01 \x01(\x04\x12\x0c\n\x04gain\x18\x02 \x01(\r\"A\n\x0fNodePerformance\x12.\n\x05\x66lows\x18\x01 \x03(\x0b\x32\x1f.aiCommunicator.FlowPerformance\"/\n\x0f\x46lowPerformance\x12\x0f\n\x07\x66low_id\x18\x01 \x01(\r\x12\x0b\n\x03\x62ps\x18\x02 \x01(\r\"\xc9\x01\n\rGatewayReport\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\x04\x12\x15\n\rend_timestamp\x18\x02 \x01(\x04\x12*\n\x08location\x18\x03 \x01(\x0b\x32\x18.aiCommunicator.Location\x12,\n\x05slots\x18\x04 \x03(\x0b\x32\x1d.aiCommunicator.InternalVoxel\x12.\n\x05\x66lows\x18\x05 \x03(\x0b\x32\x1f.aiCommunicator.FlowPerformance\"\x92\x03\n\nInternalAI\x12\x13\n\x0bstatementID\x18\x01 \x01(\x04\x12\x13\n\x0bmac_address\x18\x02 \x01(\x04\x12\x11\n\tnodeIndex\x18\x03 \x01(\x05\x12\x32\n\tgw_report\x18\x65 \x01(\x0b\x32\x1d.aiCommunicator.GatewayReportH\x00\x12\x35\n\nslot_alloc\x18\x66 \x01(\x0b\x32\x1f.aiCommunicator.TXSlotAllocatedH\x00\x12\x35\n\x0cslot_removed\x18g \x01(\x0b\x32\x1d.aiCommunicator.TXSlotRemovedH\x00\x12\x35\n\x0cgain_changed\x18h \x01(\x0b\x32\x1d.aiCommunicator.TXGainChangedH\x00\x12\x33\n\x08nodeperf\x18i \x01(\x0b\x32\x1f.aiCommunicator.NodePerformanceH\x00\x12\'\n\x05query\x18\xca\x01 \x01(\x0e\x32\x15.aiCommunicator.QueryH\x00\x42\t\n\x07payloadJ\x05\x08k\x10\xc9\x01*N\n\x05Query\x12\x11\n\rQUERY_UNKNOWN\x10\x00\x12\x19\n\x14QUERY_WHO_IS_GATEWAY\x10\x81\x02\x12\x17\n\x12QUERY_I_AM_GATEWAY\x10\x82\x02\x62\x06proto3')
)

_QUERY = _descriptor.EnumDescriptor(
  name='Query',
  full_name='aiCommunicator.Query',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_WHO_IS_GATEWAY', index=1, number=257,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_I_AM_GATEWAY', index=2, number=258,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1094,
  serialized_end=1172,
)
_sym_db.RegisterEnumDescriptor(_QUERY)

Query = enum_type_wrapper.EnumTypeWrapper(_QUERY)
QUERY_UNKNOWN = 0
QUERY_WHO_IS_GATEWAY = 257
QUERY_I_AM_GATEWAY = 258



_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='aiCommunicator.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='longitude', full_name='aiCommunicator.Location.longitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='aiCommunicator.Location.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='aiCommunicator.Location.elevation', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=99,
)


_INTERNALVOXEL = _descriptor.Descriptor(
  name='InternalVoxel',
  full_name='aiCommunicator.InternalVoxel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeslot', full_name='aiCommunicator.InternalVoxel.timeslot', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='aiCommunicator.InternalVoxel.channel', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dst', full_name='aiCommunicator.InternalVoxel.dst', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validitystart', full_name='aiCommunicator.InternalVoxel.validitystart', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tx_gain', full_name='aiCommunicator.InternalVoxel.tx_gain', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=204,
)


_TXSLOTALLOCATED = _descriptor.Descriptor(
  name='TXSlotAllocated',
  full_name='aiCommunicator.TXSlotAllocated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dst', full_name='aiCommunicator.TXSlotAllocated.dst', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeslot', full_name='aiCommunicator.TXSlotAllocated.timeslot', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='aiCommunicator.TXSlotAllocated.channel', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=271,
)


_TXSLOTREMOVED = _descriptor.Descriptor(
  name='TXSlotRemoved',
  full_name='aiCommunicator.TXSlotRemoved',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeslot', full_name='aiCommunicator.TXSlotRemoved.timeslot', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='aiCommunicator.TXSlotRemoved.channel', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=323,
)


_TXGAINCHANGED = _descriptor.Descriptor(
  name='TXGainChanged',
  full_name='aiCommunicator.TXGainChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dst', full_name='aiCommunicator.TXGainChanged.dst', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='aiCommunicator.TXGainChanged.gain', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=367,
)


_NODEPERFORMANCE = _descriptor.Descriptor(
  name='NodePerformance',
  full_name='aiCommunicator.NodePerformance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flows', full_name='aiCommunicator.NodePerformance.flows', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=434,
)


_FLOWPERFORMANCE = _descriptor.Descriptor(
  name='FlowPerformance',
  full_name='aiCommunicator.FlowPerformance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flow_id', full_name='aiCommunicator.FlowPerformance.flow_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bps', full_name='aiCommunicator.FlowPerformance.bps', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=483,
)


_GATEWAYREPORT = _descriptor.Descriptor(
  name='GatewayReport',
  full_name='aiCommunicator.GatewayReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='aiCommunicator.GatewayReport.start_timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='aiCommunicator.GatewayReport.end_timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='aiCommunicator.GatewayReport.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slots', full_name='aiCommunicator.GatewayReport.slots', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flows', full_name='aiCommunicator.GatewayReport.flows', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=687,
)


_INTERNALAI = _descriptor.Descriptor(
  name='InternalAI',
  full_name='aiCommunicator.InternalAI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statementID', full_name='aiCommunicator.InternalAI.statementID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac_address', full_name='aiCommunicator.InternalAI.mac_address', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodeIndex', full_name='aiCommunicator.InternalAI.nodeIndex', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gw_report', full_name='aiCommunicator.InternalAI.gw_report', index=3,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_alloc', full_name='aiCommunicator.InternalAI.slot_alloc', index=4,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_removed', full_name='aiCommunicator.InternalAI.slot_removed', index=5,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain_changed', full_name='aiCommunicator.InternalAI.gain_changed', index=6,
      number=104, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodeperf', full_name='aiCommunicator.InternalAI.nodeperf', index=7,
      number=105, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query', full_name='aiCommunicator.InternalAI.query', index=8,
      number=202, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='aiCommunicator.InternalAI.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=690,
  serialized_end=1092,
)

_NODEPERFORMANCE.fields_by_name['flows'].message_type = _FLOWPERFORMANCE
_GATEWAYREPORT.fields_by_name['location'].message_type = _LOCATION
_GATEWAYREPORT.fields_by_name['slots'].message_type = _INTERNALVOXEL
_GATEWAYREPORT.fields_by_name['flows'].message_type = _FLOWPERFORMANCE
_INTERNALAI.fields_by_name['gw_report'].message_type = _GATEWAYREPORT
_INTERNALAI.fields_by_name['slot_alloc'].message_type = _TXSLOTALLOCATED
_INTERNALAI.fields_by_name['slot_removed'].message_type = _TXSLOTREMOVED
_INTERNALAI.fields_by_name['gain_changed'].message_type = _TXGAINCHANGED
_INTERNALAI.fields_by_name['nodeperf'].message_type = _NODEPERFORMANCE
_INTERNALAI.fields_by_name['query'].enum_type = _QUERY
_INTERNALAI.oneofs_by_name['payload'].fields.append(
  _INTERNALAI.fields_by_name['gw_report'])
_INTERNALAI.fields_by_name['gw_report'].containing_oneof = _INTERNALAI.oneofs_by_name['payload']
_INTERNALAI.oneofs_by_name['payload'].fields.append(
  _INTERNALAI.fields_by_name['slot_alloc'])
_INTERNALAI.fields_by_name['slot_alloc'].containing_oneof = _INTERNALAI.oneofs_by_name['payload']
_INTERNALAI.oneofs_by_name['payload'].fields.append(
  _INTERNALAI.fields_by_name['slot_removed'])
_INTERNALAI.fields_by_name['slot_removed'].containing_oneof = _INTERNALAI.oneofs_by_name['payload']
_INTERNALAI.oneofs_by_name['payload'].fields.append(
  _INTERNALAI.fields_by_name['gain_changed'])
_INTERNALAI.fields_by_name['gain_changed'].containing_oneof = _INTERNALAI.oneofs_by_name['payload']
_INTERNALAI.oneofs_by_name['payload'].fields.append(
  _INTERNALAI.fields_by_name['nodeperf'])
_INTERNALAI.fields_by_name['nodeperf'].containing_oneof = _INTERNALAI.oneofs_by_name['payload']
_INTERNALAI.oneofs_by_name['payload'].fields.append(
  _INTERNALAI.fields_by_name['query'])
_INTERNALAI.fields_by_name['query'].containing_oneof = _INTERNALAI.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['InternalVoxel'] = _INTERNALVOXEL
DESCRIPTOR.message_types_by_name['TXSlotAllocated'] = _TXSLOTALLOCATED
DESCRIPTOR.message_types_by_name['TXSlotRemoved'] = _TXSLOTREMOVED
DESCRIPTOR.message_types_by_name['TXGainChanged'] = _TXGAINCHANGED
DESCRIPTOR.message_types_by_name['NodePerformance'] = _NODEPERFORMANCE
DESCRIPTOR.message_types_by_name['FlowPerformance'] = _FLOWPERFORMANCE
DESCRIPTOR.message_types_by_name['GatewayReport'] = _GATEWAYREPORT
DESCRIPTOR.message_types_by_name['InternalAI'] = _INTERNALAI
DESCRIPTOR.enum_types_by_name['Query'] = _QUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.Location)
  ))
_sym_db.RegisterMessage(Location)

InternalVoxel = _reflection.GeneratedProtocolMessageType('InternalVoxel', (_message.Message,), dict(
  DESCRIPTOR = _INTERNALVOXEL,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.InternalVoxel)
  ))
_sym_db.RegisterMessage(InternalVoxel)

TXSlotAllocated = _reflection.GeneratedProtocolMessageType('TXSlotAllocated', (_message.Message,), dict(
  DESCRIPTOR = _TXSLOTALLOCATED,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.TXSlotAllocated)
  ))
_sym_db.RegisterMessage(TXSlotAllocated)

TXSlotRemoved = _reflection.GeneratedProtocolMessageType('TXSlotRemoved', (_message.Message,), dict(
  DESCRIPTOR = _TXSLOTREMOVED,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.TXSlotRemoved)
  ))
_sym_db.RegisterMessage(TXSlotRemoved)

TXGainChanged = _reflection.GeneratedProtocolMessageType('TXGainChanged', (_message.Message,), dict(
  DESCRIPTOR = _TXGAINCHANGED,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.TXGainChanged)
  ))
_sym_db.RegisterMessage(TXGainChanged)

NodePerformance = _reflection.GeneratedProtocolMessageType('NodePerformance', (_message.Message,), dict(
  DESCRIPTOR = _NODEPERFORMANCE,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.NodePerformance)
  ))
_sym_db.RegisterMessage(NodePerformance)

FlowPerformance = _reflection.GeneratedProtocolMessageType('FlowPerformance', (_message.Message,), dict(
  DESCRIPTOR = _FLOWPERFORMANCE,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.FlowPerformance)
  ))
_sym_db.RegisterMessage(FlowPerformance)

GatewayReport = _reflection.GeneratedProtocolMessageType('GatewayReport', (_message.Message,), dict(
  DESCRIPTOR = _GATEWAYREPORT,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.GatewayReport)
  ))
_sym_db.RegisterMessage(GatewayReport)

InternalAI = _reflection.GeneratedProtocolMessageType('InternalAI', (_message.Message,), dict(
  DESCRIPTOR = _INTERNALAI,
  __module__ = 'interAI_pb2'
  # @@protoc_insertion_point(class_scope:aiCommunicator.InternalAI)
  ))
_sym_db.RegisterMessage(InternalAI)


# @@protoc_insertion_point(module_scope)
