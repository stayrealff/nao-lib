# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.51487, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.51487, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.51487, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.38746, [ 3, -0.60000, 0.10435], [ 3, 0.33333, -0.05797]], [ 0.02793, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("HeadYaw")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.00464, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.00464, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.00464, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.00464, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.00464, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnklePitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.07052, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.07052, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.07052, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.07052, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.07052, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnkleRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.10734, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.10734, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.10734, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.10734, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.10734, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -1.33692, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -1.05418, [ 3, -0.03333, -0.07765], [ 3, 0.13333, 0.31059]], [ -0.17221, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.52018, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.52018, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -1.55509, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -1.23317, [ 3, -0.03333, -0.03969], [ 3, 0.13333, 0.15877]], [ -0.95971, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -1.20776, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -1.20776, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.00401, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.00401, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00436, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.00436, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00436, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipPitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.20406, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.20406, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.20406, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.20406, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.20406, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.11202, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.11202, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.11202, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.11202, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.11202, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipYawPitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.16103, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.16103, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.16103, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.16103, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.16103, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LKneePitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.09055, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.09055, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.09055, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.09055, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.09055, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 1.62490, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 1.62490, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.71563, [ 3, -0.13333, -0.00097], [ 3, 0.60000, 0.00436]], [ 1.72000, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 1.72000, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.36652, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.36652, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.25216, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.27247, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.27247, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.59690, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.59690, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.43110, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.00000, [ 3, -0.60000, -0.00000], [ 3, 0.33333, 0.00000]], [ 0.00000, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnklePitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.06294, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.06294, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.06294, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.06294, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.06294, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnkleRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.06600, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.06600, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.06600, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.06600, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.06600, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 1.02625, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.79936, [ 3, -0.03333, 0.06784], [ 3, 0.13333, -0.27134]], [ 0.00873, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.40653, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.40653, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 1.25140, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.94771, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.95166, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.95059, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.95059, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.00716, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.00716, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.00716, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.00716, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.00716, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipPitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.18864, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.18864, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.18864, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.18864, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.18864, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.06745, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.06745, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.06745, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.06745, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.06745, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipYawPitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.16103, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.16103, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.16103, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.16103, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.16103, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RKneePitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.07359, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.07359, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.07359, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.07359, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.07359, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 1.42419, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 1.42419, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.42536, [ 3, -0.13333, -0.00117], [ 3, 0.60000, 0.00527]], [ 1.49937, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 1.49937, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ -0.50091, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ -0.50091, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ -0.15310, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ -0.18200, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ -0.18200, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 1.50000, 1.60000, 2.00000, 3.80000, 4.80000])
keys.append([ [ 0.23213, [ 3, -0.50000, 0.00000], [ 3, 0.03333, 0.00000]], [ 0.23213, [ 3, -0.03333, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.26529, [ 3, -0.13333, 0.00000], [ 3, 0.60000, 0.00000]], [ 0.26529, [ 3, -0.60000, 0.00000], [ 3, 0.33333, 0.00000]], [ 0.26529, [ 3, -0.33333, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
