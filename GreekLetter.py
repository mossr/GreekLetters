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
		# double underscore __ for superscripts
		# single underscore _ for subscripts
		mathmappings = {
		'ismember': 'ϵ',
		'partial': '∂',
		'therefore': '∴',
		'integral': '∫',
		'le': '≤',
		'ge': '≥',
		'SUM': 'Σ',
		'sqrt': '√',
		'__0': '⁰',
		'__1': '¹',
		'__2': '²',
		'__3': '³',
		'__4': '⁴',
		'__5': '⁵',
		'__6': '⁶',
		'__7': '⁷',
		'__8': '⁸',
		'__9': '⁹',
		'__a': 'ᵃ',
		'__b': 'ᵇ',
		'__c': 'ᶜ',
		'__d': 'ᵈ',
		'__e': 'ᵉ',
		'__f': 'ᶠ',
		'__g': 'ᵍ',
		'__h': 'ʰ',
		'__i': 'ⁱ',
		'__j': 'ʲ',
		'__k': 'ᵏ',
		'__l': 'ˡ',
		'__m': 'ᵐ',
		'__n': 'ⁿ',
		'__o': 'ᵒ',
		'__p': 'ᵖ',
		'__r': 'ʳ',
		'__s': 'ˢ',
		'__t': 'ᵗ',
		'__u': 'ᵘ',
		'__v': 'ᵛ',
		'__w': 'ʷ',
		'__x': 'ˣ',
		'__y': 'ʸ',
		'__z': 'ᶻ',
		'__T': 'ᵀ',
		'__plus': '⁺',
		'__minus': '⁻',
		'__equal': '⁼',
		'__lpar': '⁽',
		'__rpar': '⁾',
		'_0': '₀',
		'_1': '₁',
		'_2': '₂',
		'_3': '₃',
		'_4': '₄',
		'_5': '₅',
		'_6': '₆',
		'_7': '₇',
		'_8': '₈',
		'_9': '₉',
		'_i': 'ᵢ',
		'_plus': '₊',
		'_minus': '₋',
		'_equal': '₌',
		'_lpar': '₍',
		'_rpar': '₎'
		}
		self.view.run_command("expand_selection",{"to": "word"})
		sels = self.view.sel()
		for sel in sels:
			key = self.view.substr(sel)
			if key in greekmappings:
				replacement = greekmappings[key]
				self.view.replace(edit,sel,replacement.decode('utf-8'))
			elif key in mathmappings:
				replacement = mathmappings[key]
				if self.view.substr(sublime.Region(sel.a-1, sel.a)) == ' ':
					sel = sublime.Region(sel.a-1, sel.b)
				self.view.replace(edit,sel,replacement.decode('utf-8'))				
		end = self.view.sel()[0].b
		pt = sublime.Region(end, end)
		self.view.sel().clear()
		self.view.sel().add(pt)
