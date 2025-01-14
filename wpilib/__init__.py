# TODO: robotpy-build subpackage bug
from wpimath._controls._controls import trajectory as _

from . import _init_wpilib
from ._impl.main import run

# autogenerated by 'robotpy-build create-imports wpilib'
from ._wpilib import (
    ADIS16448_IMU,
    ADIS16470_IMU,
    ADXL345_I2C,
    ADXL345_SPI,
    ADXL362,
    CAN,
    DMC60,
    I2C,
    PWM,
    SD540,
    SPI,
    AddressableLED,
    ADXRS450_Gyro,
    AnalogAccelerometer,
    AnalogEncoder,
    AnalogGyro,
    AnalogInput,
    AnalogOutput,
    AnalogPotentiometer,
    AnalogTrigger,
    AnalogTriggerOutput,
    AnalogTriggerType,
    BuiltInAccelerometer,
    CANData,
    CANStatus,
    Color,
    Color8Bit,
    Compressor,
    CompressorConfigType,
    Counter,
    DataLogManager,
    DigitalGlitchFilter,
    DigitalInput,
    DigitalOutput,
    DigitalSource,
    DoubleSolenoid,
    DriverStation,
    DSControlWord,
    DutyCycle,
    DutyCycleEncoder,
    Encoder,
    Field2d,
    FieldObject2d,
    IterativeRobotBase,
    Jaguar,
    Joystick,
    LiveWindow,
    Mechanism2d,
    MechanismLigament2d,
    MechanismObject2d,
    MechanismRoot2d,
    MotorControllerGroup,
    MotorSafety,
    NidecBrushless,
    Notifier,
    PneumaticHub,
    PneumaticsBase,
    PneumaticsControlModule,
    PneumaticsModuleType,
    PowerDistribution,
    Preferences,
    PS4Controller,
    PWMMotorController,
    PWMSparkMax,
    PWMTalonFX,
    PWMTalonSRX,
    PWMVenom,
    PWMVictorSPX,
    Relay,
    RobotBase,
    RobotController,
    RobotState,
    RuntimeType,
    SendableBuilderImpl,
    SendableChooser,
    SendableChooserBase,
    SensorUtil,
    SerialPort,
    Servo,
    SmartDashboard,
    Solenoid,
    Spark,
    SynchronousInterrupt,
    Talon,
    TimedRobot,
    Timer,
    TimesliceRobot,
    Tracer,
    Ultrasonic,
    Victor,
    VictorSP,
    Watchdog,
    XboxController,
    getCurrentThreadPriority,
    getDeployDirectory,
    getErrorMessage,
    getOperatingDirectory,
    getTime,
    setCurrentThreadPriority,
    wait,
)
from .cameraserver import CameraServer
from .deployinfo import getDeployData

__all__ = [
    "ADIS16448_IMU",
    "ADIS16470_IMU",
    "ADXL345_I2C",
    "ADXL345_SPI",
    "ADXL362",
    "ADXRS450_Gyro",
    "AddressableLED",
    "AnalogAccelerometer",
    "AnalogEncoder",
    "AnalogGyro",
    "AnalogInput",
    "AnalogOutput",
    "AnalogPotentiometer",
    "AnalogTrigger",
    "AnalogTriggerOutput",
    "AnalogTriggerType",
    "BuiltInAccelerometer",
    "CAN",
    "CANData",
    "CANStatus",
    "Color",
    "Color8Bit",
    "Compressor",
    "CompressorConfigType",
    "Counter",
    "DataLogManager",
    "DMC60",
    "DSControlWord",
    "DigitalGlitchFilter",
    "DigitalInput",
    "DigitalOutput",
    "DigitalSource",
    "DoubleSolenoid",
    "DriverStation",
    "DutyCycle",
    "DutyCycleEncoder",
    "Encoder",
    "Field2d",
    "FieldObject2d",
    "I2C",
    "IterativeRobotBase",
    "Jaguar",
    "Joystick",
    "LiveWindow",
    "Mechanism2d",
    "MechanismLigament2d",
    "MechanismObject2d",
    "MechanismRoot2d",
    "MotorControllerGroup",
    "MotorSafety",
    "NidecBrushless",
    "Notifier",
    "PS4Controller",
    "PWM",
    "PWMMotorController",
    "PWMSparkMax",
    "PWMTalonFX",
    "PWMTalonSRX",
    "PWMVenom",
    "PWMVictorSPX",
    "PneumaticHub",
    "PneumaticsBase",
    "PneumaticsControlModule",
    "PneumaticsModuleType",
    "PowerDistribution",
    "Preferences",
    "Relay",
    "RobotBase",
    "RobotController",
    "RobotState",
    "RuntimeType",
    "SD540",
    "SPI",
    "SendableBuilderImpl",
    "SendableChooser",
    "SendableChooserBase",
    "SensorUtil",
    "SerialPort",
    "Servo",
    "SmartDashboard",
    "Solenoid",
    "Spark",
    "SynchronousInterrupt",
    "Talon",
    "TimedRobot",
    "Timer",
    "TimesliceRobot",
    "Tracer",
    "Ultrasonic",
    "Victor",
    "VictorSP",
    "Watchdog",
    "XboxController",
    "getCurrentThreadPriority",
    "getDeployDirectory",
    "getErrorMessage",
    "getOperatingDirectory",
    "getTime",
    "setCurrentThreadPriority",
    "wait",
]

# Error reporting
from ._impl.report_error import reportError, reportWarning

__all__ += ["reportError", "reportWarning"]

del _init_wpilib


try:
    from .version import version as __version__
except ImportError:
    __version__ = "master"


__all__ += ["CameraServer", "run"]
