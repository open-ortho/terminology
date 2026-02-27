[ ] Add bolton valueset

code,meaning Original medium
L,Lateral Ceph,Acetate Film
F,Frontal Ceph,Acetate Film
P,Pelvis,Acetate Film
FA,Foot & Ankle,Acetate Film
H,Hand & Wrist,Acetate Film
RE,Record of Examination,Paper
RF,Record of Facial and Jaw Examination,Paper
SM,Scan of Study Model,Gypsum
FM,Scan of Facial Moulage,Gypsum

[ ] Add new Concept Map to map the bolton value set to SNOMED codes using these codes:

                    'Lateral': '201456002', // 'Cephalogram'
                    'Hip & Pelvis': '268425006', // 'Pelvis X-ray'
                    'Foot & Ankle': '1597004', // 'Skeletal X-ray of ankle and foot'
                    'Hand & Wrist': '39714003', // 'Skeletal X-ray of wrist and hand'
                    // 'Elbow': '1927002', // 'Entire left elbow region'
                    // 'Elbow': '71889004', // 'Entire right elbow region'
                    // 'Knee': '210659002', // 'Entire left knee'
                    // 'Knee': '210562007', // 'Entire right knee'
                    // 'Frontal' -> Look up, should be PA Cephalogram, or something like that.
                    // 'Chest & Shoulder' -> Can i map to two code? Look up both codes. Or is there a code that encompasses both? Maybe i should use only shoulder, because the radiograph really only shows part of the Chest.
