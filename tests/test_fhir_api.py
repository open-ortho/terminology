import unittest
from fastapi.testclient import TestClient
from terminology.server.fhir_api import app
from terminology.resources.value_sets.dicom_scheduled_protocol import DicomScheduledProtocol

class TestFHIRAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    # def test_fhir_terminology_lookup(self):
    #     # Assuming you have a specific code to lookup
    #     code = "example-code"
    #     system = "http://example.org/fhir/CodeSystem/example-system"
    #     response = self.client.get(f"/CodeSystem/$lookup?code={code}&system={system}")
    #     self.assertEqual(response.status_code, 200)
    #     data = response.json()
    #     self.assertIn("resourceType", data)
    #     self.assertEqual(data["resourceType"], "Parameters")
    #     self.assertIn("parameter", data)

    # def test_fhir_terminology_translation(self):
    #     # Assuming you have a specific code to translate
    #     code = "example-code"
    #     source_system = "http://example.org/fhir/CodeSystem/source-system"
    #     target_system = "http://example.org/fhir/CodeSystem/target-system"
    #     response = self.client.get(f"/ConceptMap/$translate?code={code}&system={source_system}&targetsystem={target_system}")
    #     self.assertEqual(response.status_code, 200)
    #     data = response.json()
    #     self.assertIn("resourceType", data)
    #     self.assertEqual(data["resourceType"], "Parameters")
    #     self.assertIn("parameter", data)
    #     # Add more assertions based on the expected translation result

    def test_expand_valueset(self):
        # Test the GET request for expand_valueset
        url = DicomScheduledProtocol.static_url
        response = self.client.get(f"/ValueSet/$expand?url={url}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("resourceType", data)
        self.assertEqual(data["resourceType"], "ValueSet")
        self.assertIn("url", data)
        self.assertEqual(data["url"], DicomScheduledProtocol.static_url)
        self.assertIn("expansion", data)
        self.assertIn("contains", data["expansion"])
        expected_concepts = [
            {"system": concept["system"], "code": concept["code"], "display": concept["display"]}
            for concept in DicomScheduledProtocol().compose["include"][0]["concept"]
        ]
        self.assertEqual(data["expansion"]["contains"], expected_concepts)


if __name__ == '__main__':
    unittest.main()