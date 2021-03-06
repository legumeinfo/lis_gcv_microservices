# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/chromosome.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromosome.structures import chromosome_pb2 as structures_dot_chromosome__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/chromosome.proto',
  package='gcv.services',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19services/chromosome.proto\x12\x0cgcv.services\x1a\x1bstructures/chromosome.proto\"$\n\x14\x43hromosomeGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"D\n\x12\x43hromosomeGetReply\x12.\n\nchromosome\x18\x01 \x01(\x0b\x32\x1a.gcv.structures.Chromosome2[\n\nChromosome\x12M\n\x03Get\x12\".gcv.services.ChromosomeGetRequest\x1a .gcv.services.ChromosomeGetReply\"\x00\x62\x06proto3'
  ,
  dependencies=[structures_dot_chromosome__pb2.DESCRIPTOR,])




_CHROMOSOMEGETREQUEST = _descriptor.Descriptor(
  name='ChromosomeGetRequest',
  full_name='gcv.services.ChromosomeGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gcv.services.ChromosomeGetRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=72,
  serialized_end=108,
)


_CHROMOSOMEGETREPLY = _descriptor.Descriptor(
  name='ChromosomeGetReply',
  full_name='gcv.services.ChromosomeGetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chromosome', full_name='gcv.services.ChromosomeGetReply.chromosome', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=110,
  serialized_end=178,
)

_CHROMOSOMEGETREPLY.fields_by_name['chromosome'].message_type = structures_dot_chromosome__pb2._CHROMOSOME
DESCRIPTOR.message_types_by_name['ChromosomeGetRequest'] = _CHROMOSOMEGETREQUEST
DESCRIPTOR.message_types_by_name['ChromosomeGetReply'] = _CHROMOSOMEGETREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChromosomeGetRequest = _reflection.GeneratedProtocolMessageType('ChromosomeGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHROMOSOMEGETREQUEST,
  '__module__' : 'services.chromosome_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.ChromosomeGetRequest)
  })
_sym_db.RegisterMessage(ChromosomeGetRequest)

ChromosomeGetReply = _reflection.GeneratedProtocolMessageType('ChromosomeGetReply', (_message.Message,), {
  'DESCRIPTOR' : _CHROMOSOMEGETREPLY,
  '__module__' : 'services.chromosome_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.ChromosomeGetReply)
  })
_sym_db.RegisterMessage(ChromosomeGetReply)



_CHROMOSOME = _descriptor.ServiceDescriptor(
  name='Chromosome',
  full_name='gcv.services.Chromosome',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=180,
  serialized_end=271,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='gcv.services.Chromosome.Get',
    index=0,
    containing_service=None,
    input_type=_CHROMOSOMEGETREQUEST,
    output_type=_CHROMOSOMEGETREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHROMOSOME)

DESCRIPTOR.services_by_name['Chromosome'] = _CHROMOSOME

# @@protoc_insertion_point(module_scope)
