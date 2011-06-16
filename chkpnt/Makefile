#
#
#
TOP = ..
include $(TOP)/Make.misc

.SUFFIXES: .o

CFLAGS_ECHKPNT = $(EXTERN_CFLAGS)
# LSF lib 

LSFLIB = $(TOP)/lsf/lib/liblsf.a

# The debug flag will be used by generic echkpnt and generic erestart
DEBUG = -DDEBUG

# generic echkpnt and generic erestart object file
OBJECTS = echkpnt.o erestart.o
OBJ_ECHKPNT_LIBS = echkpnt.env.o echkpnt.lib.o

# generic echkpnt and generic erestart header file
H_ECHKPNT_LIBS = echkpnt.env.h echkpnt.lib.h

# generic echkpnt and erestart binary  
BINARIES = echkpnt erestart

OBJ_CMD = $(OBJECTS) $(OBJ_ECHKPNT_LIBS)

.c.o: $<
	$(CC) $(CFLAGS) -c -o $@ $<
	
build all: $(BINARIES) 

clean:
	rm -f $(OBJ_CMD)
	rm -f $(BINARIES) core

lint	:
	lint -Ae $(DEFINES) *.c

install: build
	mkdir -p $(OPENLAVA_SBINDIR); \
	install -m 755 $(BINARIES) $(OPENLAVA_SBINDIR)

$(LSFLIB):
	cd $(@D); $(MAKE)
#
# build the object file of generic echkpnt and erestart, these object file can not use the suffix rule
#

echkpnt.env.o : echkpnt.env.c  $(H_ECHKPNT_LIBS)
	$(CC) $(CFLAGS_ECHKPNT) -c $*.c

echkpnt.lib.o : echkpnt.lib.c  $(H_ECHKPNT_LIBS)
	$(CC) $(CFLAGS_ECHKPNT) -c $*.c

echkpnt.o : echkpnt.c  $(H_ECHKPNT_LIBS)
	$(CC) $(CFLAGS_ECHKPNT) -c $*.c

erestart.o : erestart.c  $(H_ECHKPNT_LIBS)
	$(CC) $(CFLAGS_ECHKPNT) -c $*.c

# Build the command echkpnt and erestart
#
$(BINARIES) : $(OBJECTS) $(OBJ_ECHKPNT_LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS_ECHKPNT) -o $@ $@.o $(OBJ_ECHKPNT_LIBS) $(ECHKPNT_LIBS) $(LSFLIB) $(LDLLIB)

$(OBJ_DEF_ECHKPNT) $(OBJ_DEF_ERESTART) : $(HFILES)

