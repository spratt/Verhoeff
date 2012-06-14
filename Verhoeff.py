#!`which python`

# Copyright (c) 2012, Simon David Pratt <me@simondavidpratt.com>
                                                                 
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all
# copies.
                                                                 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
# PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

d_table = [[0,1,2,3,4,5,6,7,8,9],
           [1,2,3,4,0,6,7,8,9,5],
           [2,3,4,0,1,7,8,9,5,6],
           [3,4,0,1,2,8,9,5,6,7],
           [4,0,1,2,3,9,5,6,7,8],
           [5,9,8,7,6,0,4,3,2,1],
           [6,5,9,8,7,1,0,4,3,2],
           [7,6,5,9,8,2,1,0,4,3],
           [8,7,6,5,9,3,2,1,0,4],
           [9,8,7,6,5,4,3,2,1,0]]

def d(j,k):
    return d_table[j][k]

p_table = [[0,1,2,3,4,5,6,7,8,9],
           [1,5,7,6,2,8,3,0,9,4],
           [5,8,0,3,7,9,6,1,4,2],
           [8,9,1,6,0,4,3,5,2,7],
           [9,4,5,3,1,2,6,8,7,0],
           [4,2,8,6,5,7,3,9,0,1],
           [2,7,9,3,8,0,6,4,1,5],
           [7,0,4,6,9,1,3,2,5,8]]

def p(pos,num):
    return p_table[pos%8][num]

def checksum(digits_str):
    c=0
    l = len(digits_str)-1
    for i in range(0,l):
        c=d(c,p(i,int(digits_str[l-i])))
    return c

def verify(digits_str):
    return checksum(digits_str[:-1]) == int(digits_str[-1])
