# python -m unittest test_summarizer.py
import unittest
from app.summarizer import summarize_text

class TestSummarizer(unittest.TestCase):
    def test_summarize_text(self):
        text = "Russia has been increasing its activity along the Finnish border, according to areport by the New York TimesOpens an external website, with satellite imagery revealing large tents, shelters for fighter jets and warehouses for military vehicles. While reporting that Russia is strengthening its military bases in the area, on the Karelian Isthmus, the newspaper noted the activity is nothing like the buildup along the Ukraine border before Russia's full-scale invasion in 2022. For now, Russia, preoccupied with its war in Ukraine, has very few troops along the frontier, and the Finns insist that none of this is much of a threat — yet, the NYT article added. Ylereported in Januarythat Russia was increasing its presence in the region near Finland's southeastern frontier, but even the Russian troops stationed there were focused on the war in Ukraine. From Finland's perspective, the situation remains stable. Russia lacks the resources to bolster its military presence near Finland and is instead directing additional troops and equipment towards the conflict in Ukraine, Yle reported at the time. Satellite images released at the time showed the construction of a maintenance hall at a vast equipment depot in Petrozavodsk, 175 kilometres east of the Finnish border, which could accommodate about 2,000 soldiers. The satellite images below show the increase in the number of tents since last summer. Military expertMarko Eklund, who analysed the satellite images for Yle, said at the time that the training centre was being used by troops preparing to join the war in Ukraine. The NYT article further noted that Finnish authorities have remained characteristically matter of fact about the reported increase in Russian activity, with one military official saying Finland is preparing for a tripling in the number of Russian troops in the border region once the Ukraine war is over."
        summary = summarize_text(text)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
        self.assertLessEqual(len(summary), 500)
        
if __name__ == "__main__":
    unittest.main()  # Ensure the summary is shorter than the original text