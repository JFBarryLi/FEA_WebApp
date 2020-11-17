TrussExampleInput = {
    "matProp": {
        "ele1": {
            "index": 0,
            "E": 2000000,
            "A": 2
        },
        "ele2": {
            "index": 1,
            "E": 2000000,
            "A": 2
        },
        "ele3": {
            "index": 2,
            "E": 2000000,
            "A": 1
        },
        "ele4": {
            "index": 3,
            "E": 2000000,
            "A": 1
        }
    },
    "nodalCoords": {
        "node1": {
            "index": 0,
            "x": 0,
            "y": 0,
            "z": 0
        },
        "node2": {
            "index": 1,
            "x": 100,
            "y": 0,
            "z": 0
        },
        "node3": {
            "index": 2,
            "x": 50,
            "y": 50,
            "z": 0
        },
        "node4": {
            "index": 3,
            "x": 200,
            "y": 100,
            "z": 0
        }
    },
    "connectivity": {
        "ele1": {
            "index": 0,
            "i": "node1",
            "j": "node3"
        },
        "ele2": {
            "index": 1,
            "i": "node3",
            "j": "node2"
        },
        "ele3": {
            "index": 2,
            "i": "node3",
            "j": "node4"
        },
        "ele4": {
            "index": 3,
            "i": "node2",
            "j": "node4"
        }
    },
    "forceVector": {
        "node4": {
            "index": 3,
            "forces": {
                "u1": {
                    "index": 0,
                    "value": 0
                },
                "u2": {
                    "index": 1,
                    "value": -1000
                },
                "u3": {
                    "index": 2,
                    "value": 0
                }
            }
        }
    },
    "boundaryConditions": {
        "node1": {
            "index": 0,
            "bc": {
                "u1": {
                    "index": 0,
                    "value": 0
                },
                "u2": {
                    "index": 1,
                    "value": 0
                },
                "u3": {
                    "index": 2,
                    "value": 0
                }
            }
        },
        "node2": {
            "index": 1,
            "bc": {
                "u1": {
                    "index": 0,
                    "value": 0
                },
                "u2": {
                    "index": 1,
                    "value": 0
                },
                "u3": {
                    "index": 2,
                    "value": 0
                }
            }
        },
        "node3": {
            "index": 2,
            "bc": {
                "u3": {
                    "index": 2,
                    "value": 0
                }
            }
        },
        "node4": {
            "index": 3,
            "bc": {
                "u3": {
                    "index": 2,
                    "value": 0
                }
            }
        }
    },
    "stresses": {}
}

TrussExampleOutput = {
  "matProp": {
    "ele1": {
      "index": 0,
      "E": 2000000,
      "A": 2
    },
    "ele2": {
      "index": 1,
      "E": 2000000,
      "A": 2
    },
    "ele3": {
      "index": 2,
      "E": 2000000,
      "A": 1
    },
    "ele4": {
      "index": 3,
      "E": 2000000,
      "A": 1
    }
  },
  "nodalCoords": {
    "node1": {
      "index": 0,
      "x": 0,
      "y": 0,
      "z": 0
    },
    "node2": {
      "index": 1,
      "x": 100,
      "y": 0,
      "z": 0
    },
    "node3": {
      "index": 2,
      "x": 50.0265165042945,
      "y": 50.00883883476483,
      "z": 0
    },
    "node4": {
      "index": 3,
      "x": 200.34790254476266,
      "y": 99.43996542088136,
      "z": 0
    }
  },
  "connectivity": {
    "ele1": {
      "index": 0,
      "i": "node1",
      "j": "node3"
    },
    "ele2": {
      "index": 1,
      "i": "node3",
      "j": "node2"
    },
    "ele3": {
      "index": 2,
      "i": "node3",
      "j": "node4"
    },
    "ele4": {
      "index": 3,
      "i": "node2",
      "j": "node4"
    }
  },
  "forceVector": {
    "node4": {
      "index": 3,
      "forces": {
        "u1": {
          "index": 0,
          "value": 0
        },
        "u2": {
          "index": 1,
          "value": -1000
        },
        "u3": {
          "index": 2,
          "value": 0
        }
      }
    }
  },
  "boundaryConditions": {
    "node1": {
      "index": 0,
      "bc": {
        "u1": {
          "index": 0,
          "value": 0
        },
        "u2": {
          "index": 1,
          "value": 0
        },
        "u3": {
          "index": 2,
          "value": 0
        }
      }
    },
    "node2": {
      "index": 1,
      "bc": {
        "u1": {
          "index": 0,
          "value": 0
        },
        "u2": {
          "index": 1,
          "value": 0
        },
        "u3": {
          "index": 2,
          "value": 0
        }
      }
    },
    "node3": {
      "index": 2,
      "bc": {
        "u3": {
          "index": 2,
          "value": 0
        }
      }
    },
    "node4": {
      "index": 3,
      "bc": {
        "u3": {
          "index": 2,
          "value": 0
        }
      }
    }
  },
  "stresses": {
    "ele1": 707.1067811865494,
    "ele2": -353.5533905932747,
    "ele3": 1581.138830084193,
    "ele4": -2121.320343559646
  }
}