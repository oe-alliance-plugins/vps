# -*- coding: utf-8 -*-

from . import _
from Components.ActionMap import HelpableActionMap
from Components.config import config
from Components.Sources.StaticText import StaticText
from Screens.Setup import Setup
from Screens.TextBox import TextBox

VERSION = "1.34"


class VPS_Setup(Setup):
	def __init__(self, session):
		Setup.__init__(self, session, None)
		self["key_blue"] = StaticText(_("Information"))
		self["actions"] = HelpableActionMap(self, ["ColorActions"], {
			"blue": (self.show_info, _("Show VPS plugin information screen")),
		}, prio=-1, description=_("VPS plugin Actions"))
		self.title = _("VPS Setup Version %s") % VERSION

	def createSetup(self):
		setup_list = [(_("Enable VPS-Plugin"), config.plugins.vps.enabled, _("This plugin can determine whether a programme begins earlier or lasts longer. The channel has to provide reliable data."))]
		if config.plugins.vps.enabled.value:
			setup_list.extend([
				(_("Check for PDC"), config.plugins.vps.do_PDC_check, _("Check for PDC availability on each service")),
				(_("Starting time"), config.plugins.vps.initial_time, _("If possible, x minutes before a timer starts VPS-Plugin will control whether the programme begins earlier. (0 disables feature)")),
				(_("Wakeup from Deep-Standby is allowed"), config.plugins.vps.allow_wakeup, _("If enabled and necessary, the plugin will wake up the Receiver from Deep-Standby for the defined starting time to control whether the programme begins earlier.")),
				(_("Seeking connected events"), config.plugins.vps.allow_seeking_multiple_pdc, _("If a programme is interrupted and divided into separate events, the plugin will search for the connected events.")),
				(_("VPS enabled by default"), config.plugins.vps.vps_default, _("Enable VPS by default (new timers)")),
				(_("Enable VPS on instant records"), config.plugins.vps.instanttimer, _("When yes, VPS will be enabled on instant records (stop after current event), if the channel supports VPS."))])
		self["config"].list = setup_list


	def show_info(self):
		VPS_show_info(self.session)


def VPS_show_info(session):
	session.open(
		TextBox,
		title=_("VPS-Plugin Information"),
		text=_("VPS-Plugin can react on delays arising in the startTime or endTime of a programme. VPS is only supported by certain channels!\n\nIf you enable VPS, the recording will only start, when the channel flags the programme as running.\n\nIf you select \"yes (safe mode)\", the recording is definitely starting at the latest at the startTime you defined. The recording may start earlier or last longer.\n\n\nSupported channels\n\nGermany:\n ARD and ZDF\n\nAustria:\n ORF\n\nSwitzerland:\n SF\n\nCzech Republic:\n CT\n\nIf a timer is programmed manually (not via EPG), it is necessary to set a VPS-Time to enable VPS. VPS-Time (also known as PDC) is the first published start time, e.g. given in magazines. If you set a VPS-Time, you have to leave timer name empty."),
	)
