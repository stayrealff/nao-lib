# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadYaw")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.00464, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.00464, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("HeadPitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.51411, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.44820, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.44820, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.44820, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.44820, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.44820, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.44820, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.44820, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.51411, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.95993, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.16563, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.22724, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.58748, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.10887, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00405, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.95993, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.95993, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.11202, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 1.18114, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.43570, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.17330, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00710, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipYawPitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.42586, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.42586, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00000, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipPitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.21817, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LKneePitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.69813, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnklePitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.34907, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnkleRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00000, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00000, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipPitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.21817, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.21817, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RKneePitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.69813, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.69813, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnklePitch")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ -0.34907, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.34907, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnkleRoll")
times.append([ 2.00000, 4.00000, 6.00000, 8.00000, 10.00000, 12.00000, 14.00000, 16.00000, 17.00000])
keys.append([ [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.66667, 0.00000]], [ 0.00000, [ 3, -0.66667, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00000, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err