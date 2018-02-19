from tests.boa_test import BoaTest
from boa.compiler import Compiler

from neo.Prompt.Commands.BuildNRun import TestBuild


class TestContract(BoaTest):


    def test_Concat1(self):
        output = Compiler.instance().load('example/ConcatTest.py').default
        out = output.write()

        tx, results, total_ops, engine = TestBuild(out, [], self.GetWallet1(), '','07')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetString(), 'helloworld')


    def test_Concat2(self):
        output = Compiler.instance().load('example/ConcatTest2.py').default
        out = output.write()

        tx, results, total_ops, engine = TestBuild(out, ['concat',"['hello','world']"], self.GetWallet1(), '10','07')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetString(), 'helloworld')

        tx, results, total_ops, engine = TestBuild(out, ['blah',"['hello','world']"], self.GetWallet1(), '10','07')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetBoolean(), False)

        tx, results, total_ops, engine = TestBuild(out, ['concat',"['blah']"], self.GetWallet1(), '10','07')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetBoolean(),False)

        tx, results, total_ops, engine = TestBuild(out, ['concat',"['hello','world','third']"], self.GetWallet1(), '10','07')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetString(), 'helloworld')

        tx, results, total_ops, engine = TestBuild(out, ['concat',"['1','neo']"], self.GetWallet1(), '10','07')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetString(), '\x01neo')

        tx, results, total_ops, engine = TestBuild(out, ['concat',"[1,'neo']"], self.GetWallet1(), '10','07')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetString(), '\x01neo')

# Testinvoke args need to be fixed
#        tx, results, total_ops, engine = TestBuild(out, ['concat',"[bytearray(b'\x01\xa0\x04'),bytearray(b'\x04\x02\x04')]"], self.GetWallet1(), '10','07')
#        self.assertEqual(len(results), 1)
#        self.assertEqual(results[0].GetByteArray(), bytearray(b'\x01\xa0\x04\x04\x02\x04'))

