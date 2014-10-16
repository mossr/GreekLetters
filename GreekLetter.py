#!/usr/bin/python
# -*- coding: utf-8 -*-
import sublime, sublime_plugin

class GreekLetterExpandCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		greekmappings = {
		'Alpha': 'Α',
		'alpha': 'α',
		'Beta': 'Β',
		'beta': 'β',
		'Gamma': 'Γ',
		'gamma': 'γ',
		'Delta': 'Δ',
		'delta': 'δ',
		'Epsilon': 'Ε',
		'epsilon': 'ε',
		'Zeta': 'Ζ',
		'zeta': 'ζ',
		'Eta': 'Η',
		'eta': 'η',
		'Theta': 'Θ',
		'theta': 'θ',
		'Iota': 'Ι',
		'iota': 'ι',
		'Kappa': 'Κ',
		'kappa': 'κ',
		'Lambda': 'Λ',
		'lambda': 'λ',
		'Mu': 'Μ',
		'mu': 'μ',
		'Nu': 'Ν',
		'nu': 'ν',
		'Xi': 'Ξ',
		'xi': 'ξ',
		'Omicron': 'Ο',
		'omicron': 'ο',
		'Pi': 'Π',
		'pi': 'π',
		'Rho': 'Ρ',
		'rho': 'ρ',
		'Sigma': 'Σ',
		'sigma': 'σ',
		'Tau': 'Τ',
		'tau': 'τ',
		'Upsilon': 'Υ',
		'upsilon': 'υ',
		'Phi': 'Φ',
		'phi': 'φ',
		'Chi': 'Χ',
		'chi': 'χ',
		'Psi': 'Ψ',
		'psi': 'ψ',
		'Omega': 'Ω',
		'omega': 'ω'
		}
		self.view.run_command("expand_selection",{"to": "word"})
		sels = self.view.sel()
		for sel in sels:
			key = self.view.substr(sel)
			if key in greekmappings:
				replacement = greekmappings[key]
				self.view.replace(edit,sel,replacement.decode('utf-8'))
		end = self.view.sel()[0].b
		pt = sublime.Region(end, end)
		self.view.sel().clear()
		self.view.sel().add(pt)

