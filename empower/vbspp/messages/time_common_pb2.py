# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: time_common.proto

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
  name='time_common.proto',
  package='protocol',
  syntax='proto2',
  serialized_pb=_b('\n\x11time_common.proto\x12\x08protocol\"b\n\x0bprp_dl_info\x12\x0c\n\x04rnti\x18\x01 \x01(\r\x12\x17\n\x0fharq_process_id\x18\x02 \x01(\r\x12\x13\n\x0bharq_status\x18\x03 \x03(\r\x12\x17\n\x0fserv_cell_index\x18\x04 \x01(\r\"q\n\x0bprp_ul_info\x12\x0c\n\x04rnti\x18\x01 \x01(\r\x12\x14\n\x0cul_reception\x18\x02 \x03(\r\x12\x18\n\x10reception_status\x18\x03 \x01(\r\x12\x0b\n\x03tpc\x18\x04 \x01(\r\x12\x17\n\x0fserv_cell_index\x18\x05 \x01(\r*<\n\x0fprp_harq_status\x12\x0c\n\x08PRHS_ACK\x10\x00\x12\r\n\tPRHS_NACK\x10\x01\x12\x0c\n\x08PRHS_DTX\x10\x02*H\n\x14prp_reception_status\x12\x0b\n\x07PRRS_OK\x10\x00\x12\x0f\n\x0bPRRS_NOT_OK\x10\x01\x12\x12\n\x0ePRRS_NOT_VALID\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PRP_HARQ_STATUS = _descriptor.EnumDescriptor(
  name='prp_harq_status',
  full_name='protocol.prp_harq_status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRHS_ACK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRHS_NACK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRHS_DTX', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=246,
  serialized_end=306,
)
_sym_db.RegisterEnumDescriptor(_PRP_HARQ_STATUS)

prp_harq_status = enum_type_wrapper.EnumTypeWrapper(_PRP_HARQ_STATUS)
_PRP_RECEPTION_STATUS = _descriptor.EnumDescriptor(
  name='prp_reception_status',
  full_name='protocol.prp_reception_status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRRS_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRRS_NOT_OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRRS_NOT_VALID', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=308,
  serialized_end=380,
)
_sym_db.RegisterEnumDescriptor(_PRP_RECEPTION_STATUS)

prp_reception_status = enum_type_wrapper.EnumTypeWrapper(_PRP_RECEPTION_STATUS)
PRHS_ACK = 0
PRHS_NACK = 1
PRHS_DTX = 2
PRRS_OK = 0
PRRS_NOT_OK = 1
PRRS_NOT_VALID = 2



_PRP_DL_INFO = _descriptor.Descriptor(
  name='prp_dl_info',
  full_name='protocol.prp_dl_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rnti', full_name='protocol.prp_dl_info.rnti', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='harq_process_id', full_name='protocol.prp_dl_info.harq_process_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='harq_status', full_name='protocol.prp_dl_info.harq_status', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serv_cell_index', full_name='protocol.prp_dl_info.serv_cell_index', index=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=129,
)


_PRP_UL_INFO = _descriptor.Descriptor(
  name='prp_ul_info',
  full_name='protocol.prp_ul_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rnti', full_name='protocol.prp_ul_info.rnti', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ul_reception', full_name='protocol.prp_ul_info.ul_reception', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reception_status', full_name='protocol.prp_ul_info.reception_status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tpc', full_name='protocol.prp_ul_info.tpc', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serv_cell_index', full_name='protocol.prp_ul_info.serv_cell_index', index=4,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=244,
)

DESCRIPTOR.message_types_by_name['prp_dl_info'] = _PRP_DL_INFO
DESCRIPTOR.message_types_by_name['prp_ul_info'] = _PRP_UL_INFO
DESCRIPTOR.enum_types_by_name['prp_harq_status'] = _PRP_HARQ_STATUS
DESCRIPTOR.enum_types_by_name['prp_reception_status'] = _PRP_RECEPTION_STATUS

prp_dl_info = _reflection.GeneratedProtocolMessageType('prp_dl_info', (_message.Message,), dict(
  DESCRIPTOR = _PRP_DL_INFO,
  __module__ = 'time_common_pb2'
  # @@protoc_insertion_point(class_scope:protocol.prp_dl_info)
  ))
_sym_db.RegisterMessage(prp_dl_info)

prp_ul_info = _reflection.GeneratedProtocolMessageType('prp_ul_info', (_message.Message,), dict(
  DESCRIPTOR = _PRP_UL_INFO,
  __module__ = 'time_common_pb2'
  # @@protoc_insertion_point(class_scope:protocol.prp_ul_info)
  ))
_sym_db.RegisterMessage(prp_ul_info)


# @@protoc_insertion_point(module_scope)
