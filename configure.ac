#
# openlava project
#
# Copyright (C) 2011 David Bigagli
#
AC_INIT(openlava, 1.0)
AC_CONFIG_HEADERS(config.h)
AC_PREFIX_DEFAULT([/opt/openlava-1.0])

# Set some cluster configuration variables .
AC_SUBST([openlavadmin], [openlava])
AC_ARG_VAR([openlavaadmin], "")

AC_SUBST([openlavacluster], [openlava])
AC_ARG_VAR([openlavacluster], "")

# Initialize the automake
AM_INIT_AUTOMAKE

# Clean output if possible
#m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])

# Check for programs
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_RANLIB
AC_PROG_YACC
AC_PROG_LEX
AC_PROG_LN_S
AC_PROG_MAKE_SET

#AC_DEFINE(REL_DATE, "Sep 11 2011", "Set the release date.")

# Force warnings on for gcc
if test "x$ac_compiler_gnu" = xyes; then
    CFLAGS="$CFLAGS -Wall"
fi

# Check for tcl, we try all 8.X versions
AC_CHECK_HEADER([tcl.h], [], [AC_MSG_ERROR([cannot build openlava without tcl])])
AC_CHECK_LIB([tcl8.6], [Tcl_CreateInterp], [], [
    AC_CHECK_LIB([tcl8.5], [Tcl_CreateInterp], [], [
        AC_CHECK_LIB([tcl8.4], [Tcl_CreateInterp], [], [
            AC_CHECK_LIB([tcl8.3], [Tcl_CreateInterp], [], [
                AC_CHECK_LIB([tcl8.2], [Tcl_CreateInterp], [], [
                    AC_CHECK_LIB([tcl8.1], [Tcl_CreateInterp], [], [
                        AC_CHECK_LIB([tcl8.0], [Tcl_CreateInterp], [], [
                            AC_MSG_ERROR([cannot build openlava without tcl8.*])
])])])])])])])

AC_CONFIG_FILES([
	Makefile                 \
	config/Makefile          \
	lsf/Makefile             \
	lsf/intlib/Makefile      \
	lsf/lib/Makefile         \
	lsf/lim/Makefile         \
	lsf/res/Makefile         \
	lsf/pim/Makefile         \
	lsf/lstools/Makefile     \
	lsf/lsadm/Makefile       \
	lsf/man/Makefile         \
	lsf/man/man1/Makefile    \
	lsf/man/man5/Makefile    \
	lsf/man/man8/Makefile    \
	lsbatch/Makefile         \
	lsbatch/lib/Makefile     \
	lsbatch/cmd/Makefile     \
	lsbatch/bhist/Makefile   \
	lsbatch/daemons/Makefile \
	lsbatch/man1/Makefile    \
	lsbatch/man5/Makefile    \
	lsbatch/man8/Makefile    \
	eauth/Makefile           \
	scripts/Makefile         \
	chkpnt/Makefile          \
	config/lsf.conf          \
	config/lsb.hosts         \
	config/lsb.params        \
	config/lsb.queues        \
	config/lsb.users         \
	config/lsf.cluster.openlava \
	config/lsf.shared        \
	config/lsf.task          \
	config/openlava.csh      \
	config/openlava          \
	config/openlava.setup    \
	config/openlava.sh]
)

AC_OUTPUT
