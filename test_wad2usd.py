#!/usr/bin/env python3

import unittest
from unittest.mock import Mock, MagicMock
import sys
import os

# Add the current directory to path to import wad2usd
sys.path.insert(0, os.path.dirname(__file__))

from wad2usd import Polygon

class TestPolygon(unittest.TestCase):

    def test_polygon_add_face(self):
        poly = Polygon("TEST")
        face = [0, 1, 2]
        tex_coords = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]
        poly.addFace(face, tex_coords)
        self.assertEqual(poly.getFaces(), [face])
        self.assertEqual(poly.getTextureCoords(), [tex_coords])

    def test_polygon_combine_segments_simple(self):
        # Test combining segments that form a rectangle
        class MockVertex:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        # Create shared vertex objects
        v00 = MockVertex(0, 0)
        v10 = MockVertex(1, 0)
        v11 = MockVertex(1, 1)
        v01 = MockVertex(0, 1)

        poly = Polygon("TEST")
        # Segment from (0,0) to (1,0), indices 0,1
        poly.addSegment(v00, v10, 0, 1)
        # Segment from (1,0) to (1,1), indices 1,2
        poly.addSegment(v10, v11, 1, 2)
        # Segment from (1,1) to (0,1), indices 2,3
        poly.addSegment(v11, v01, 2, 3)
        # Segment from (0,1) to (0,0), indices 3,0
        poly.addSegment(v01, v00, 3, 0)
        poly.combineSegments()
        # Should form one face: [2,1,0,3] with correct winding
        self.assertEqual(len(poly.getFaces()), 1)
        self.assertEqual(poly.getFaces()[0], [2, 1, 0, 3])

    def test_polygon_texture_coords_generation(self):
        class MockVertex:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        # Create shared vertex objects
        v00 = MockVertex(0, 0)
        v64_0 = MockVertex(64, 0)
        v64_64 = MockVertex(64, 64)
        v0_64 = MockVertex(0, 64)

        poly = Polygon("TEST")
        poly.addSegment(v00, v64_0, 0, 1)
        poly.addSegment(v64_0, v64_64, 1, 2)
        poly.addSegment(v64_64, v0_64, 2, 3)
        poly.addSegment(v0_64, v00, 3, 0)
        poly.combineSegments()
        # Texture coords in order of face vertices: v11, v10, v00, v01
        expected_coords = [(1.0, 1.0), (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)]
        self.assertEqual(poly.getTextureCoords()[0], expected_coords)

class TestUsdmap(unittest.TestCase):
    # TODO: Add tests for usdmap function with mocked WAD data
    pass

if __name__ == '__main__':
    unittest.main()
