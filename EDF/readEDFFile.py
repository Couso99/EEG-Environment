# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import os
import numpy as np

import pyedflib

import matplotlib.pyplot as plt

def read_signal_data(edf_file):
    f = pyedflib.edfreader.EdfReader(edf_file)
    signals_number = f.signals_in_file
    duration = f.file_duration
    buffers = np.empty((signals_number, np.amax(f.getNSamples())))
    for channel in range(signals_number):
        buffers[channel] = np.array(f.readSignal(channel))
    f._close()

    return buffers, duration

#
# if __name__ == '__main__':
# #    f = pyedflib.data.test_generator()
#     f = pyedflib.edfreader.EdfReader('non_trial_0.edf')
#     print("\nlibrary version: %s" % pyedflib.version.version)
#
#     print("\ngeneral header:\n")
#
#     # print("filetype: %i\n"%hdr.filetype);
#     print("edfsignals: %i" % f.signals_in_file)
#     duration = f.file_duration
#     print("file duration: %i seconds" % f.file_duration)
#     print("startdate: %i-%i-%i" % (f.getStartdatetime().day,f.getStartdatetime().month,f.getStartdatetime().year))
#     print("starttime: %i:%02i:%02i" % (f.getStartdatetime().hour,f.getStartdatetime().minute,f.getStartdatetime().second))
#     # print("patient: %s" % f.getP);
#     # print("recording: %s" % f.getPatientAdditional())
#     print("patientcode: %s" % f.getPatientCode())
#     print("gender: %s" % f.getGender())
#     print("birthdate: %s" % f.getBirthdate())
#     print("patient_name: %s" % f.getPatientName())
#     print("patient_additional: %s" % f.getPatientAdditional())
#     print("admincode: %s" % f.getAdmincode())
#     print("technician: %s" % f.getTechnician())
#     print("equipment: %s" % f.getEquipment())
#     print("recording_additional: %s" % f.getRecordingAdditional())
#     print("datarecord duration: %f seconds" % f.getFileDuration())
#     datarecords = f.datarecords_in_file
#     print("number of datarecords in the file: %i" % f.datarecords_in_file)
#     print("number of annotations in the file: %i" % f.annotations_in_file)
# #%%
#     channel = 7
#     print("\nsignal parameters for the %d.channel:\n\n" % channel)
#
#     print("label: %s" % f.getLabel(channel))
#     print("samples in file: %i" % f.getNSamples()[channel])
#     # print("samples in datarecord: %i" % f.get
#     print("physical maximum: %f" % f.getPhysicalMaximum(channel))
#     print("physical minimum: %f" % f.getPhysicalMinimum(channel))
#     print("digital maximum: %i" % f.getDigitalMaximum(channel))
#     print("digital minimum: %i" % f.getDigitalMinimum(channel))
#     print("physical dimension: %s" % f.getPhysicalDimension(channel))
#     print("prefilter: %s" % f.getPrefilter(channel))
#     print("transducer: %s" % f.getTransducer(channel))
#     print("samplefrequency: %f" % f.getSampleFrequency(channel))
#
#     annotations = f.readAnnotations()
#     for n in np.arange(f.annotations_in_file):
#         print("annotation: onset is %f    duration is %s    description is %s" % (annotations[0][n],annotations[1][n],annotations[2][n]))
#
#     buf = f.readSignal(channel)
#
#     import matplotlib.pyplot as plt
#     print(buf[:].shape)
#     print(len(buf))
#
#     print(np.amax(f.getNSamples()))
#
#     y = np.linspace(0, duration, 459000)
#     print(y.shape)
#     #plt.scatter(buf, y)
#     plt.plot(buf)
#     plt.show()
#
# #%%
#
#
# #%%
#     f._close()
#     del f
