# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/genes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from genes.structures import gene_pb2 as structures_dot_gene__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/genes.proto',
  package='gcv.services',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14services/genes.proto\x12\x0cgcv.services\x1a\x15structures/gene.proto\" \n\x0fGenesGetRequest\x12\r\n\x05names\x18\x01 \x03(\t\"4\n\rGenesGetReply\x12#\n\x05genes\x18\x01 \x03(\x0b\x32\x14.gcv.structures.Gene2L\n\x05Genes\x12\x43\n\x03Get\x12\x1d.gcv.services.GenesGetRequest\x1a\x1b.gcv.services.GenesGetReply\"\x00\x62\x06proto3'
  ,
  dependencies=[structures_dot_gene__pb2.DESCRIPTOR,])




_GENESGETREQUEST = _descriptor.Descriptor(
  name='GenesGetRequest',
  full_name='gcv.services.GenesGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='gcv.services.GenesGetRequest.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=61,
  serialized_end=93,
)


_GENESGETREPLY = _descriptor.Descriptor(
  name='GenesGetReply',
  full_name='gcv.services.GenesGetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genes', full_name='gcv.services.GenesGetReply.genes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=95,
  serialized_end=147,
)

_GENESGETREPLY.fields_by_name['genes'].message_type = structures_dot_gene__pb2._GENE
DESCRIPTOR.message_types_by_name['GenesGetRequest'] = _GENESGETREQUEST
DESCRIPTOR.message_types_by_name['GenesGetReply'] = _GENESGETREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesGetRequest = _reflection.GeneratedProtocolMessageType('GenesGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENESGETREQUEST,
  '__module__' : 'services.genes_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.GenesGetRequest)
  })
_sym_db.RegisterMessage(GenesGetRequest)

GenesGetReply = _reflection.GeneratedProtocolMessageType('GenesGetReply', (_message.Message,), {
  'DESCRIPTOR' : _GENESGETREPLY,
  '__module__' : 'services.genes_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.GenesGetReply)
  })
_sym_db.RegisterMessage(GenesGetReply)



_GENES = _descriptor.ServiceDescriptor(
  name='Genes',
  full_name='gcv.services.Genes',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=149,
  serialized_end=225,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='gcv.services.Genes.Get',
    index=0,
    containing_service=None,
    input_type=_GENESGETREQUEST,
    output_type=_GENESGETREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GENES)

DESCRIPTOR.services_by_name['Genes'] = _GENES

# @@protoc_insertion_point(module_scope)