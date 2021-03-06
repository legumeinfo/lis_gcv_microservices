# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from search.services import genesearch_pb2 as services_dot_genesearch__pb2


class GeneSearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/gcv.services.GeneSearch/Search',
                request_serializer=services_dot_genesearch__pb2.GeneSearchRequest.SerializeToString,
                response_deserializer=services_dot_genesearch__pb2.GeneSearchReply.FromString,
                )


class GeneSearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeneSearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=services_dot_genesearch__pb2.GeneSearchRequest.FromString,
                    response_serializer=services_dot_genesearch__pb2.GeneSearchReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gcv.services.GeneSearch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeneSearch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gcv.services.GeneSearch/Search',
            services_dot_genesearch__pb2.GeneSearchRequest.SerializeToString,
            services_dot_genesearch__pb2.GeneSearchReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
