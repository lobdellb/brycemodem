

import matplotlib.pyplot as plt
import numpy as np
import bitstring


def string_to_binary(s):
    return bitstring.BitArray( s.encode("utf-8") )


def make_sine_wave(durration, fs, freq ):    
    return np.sin( 2 * np.pi * np.arange(0,durration,1/fs) * freq )


def make_silence( durration, fs ):
	return np.zeros( int( durration * fs  ) )



def bytes_to_arrays(data,samplewidth=None, channels=None):
    
    factor = 2 ** (8*samplewidth-1) - 1
    
    if channels == 1:
        left = np.array( list( map( lambda d : int.from_bytes( d , "little", signed=True ) , [data[i+0:i+samplewidth+0] for i in range(0, len(data), samplewidth*channels)] ) ) ) / factor
        
        return left
        
    elif channels == 2:
        left = np.array( list( map( lambda d : int.from_bytes( d , "little", signed=True ) , [data[i+0:i+samplewidth+0] for i in range(0, len(data), samplewidth*channels)] ) ) ) / factor
        right = np.array( list( map( lambda d : int.from_bytes( d , "little", signed=True ) , [data[i+2:i+samplewidth+2] for i in range(0, len(data), samplewidth*channels)] ) ) ) / factor
        
        return left,right
        
    else:
        raise Exception("channels must be 1 or 2")






# generate an audio signal:
def normalized_wf_to_bytes( s, channels=1,width=2 ):
    
    if channels != 1:
        raise Exception("only channels=1 is implemented")
    
    factor = 2 ** (8*width-1) - 1
    
    return b"".join( map( lambda e : int(e*factor).to_bytes(width,"little", signed=True), s ) )