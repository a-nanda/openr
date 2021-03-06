#!/usr/bin/env python3

#
# Copyright (c) 2014-present, Facebook, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import object

import zmq
from fbzmq.Monitor import ttypes as monitor_types
from openr.utils import consts, zmq_socket


class MonitorSubscriber(object):
    def __init__(
        self,
        zmq_ctx,
        monitor_pub_url,
        timeout=-1,
        proto_factory=consts.Consts.PROTO_FACTORY,
    ):

        # timeout set as -1 for indefinite blocking
        self._monitor_sub_socket = zmq_socket.ZmqSocket(
            zmq_ctx, zmq.SUB, timeout, proto_factory
        )
        self._monitor_sub_socket.connect(monitor_pub_url)
        self._monitor_sub_socket.set_sock_opt(zmq.SUBSCRIBE, b"")

    def listen(self):
        return self._monitor_sub_socket.recv_thrift_obj(monitor_types.MonitorPub)
